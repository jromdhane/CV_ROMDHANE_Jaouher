#!/usr/bin/env python3
"""
CV Adapter v11.0 - 1-Page CV Optimization
ATS optimization, keyword injection, smart experience reduction for 1-page format
"""
import os, json, subprocess, re, sys, shutil, time
from pathlib import Path
from datetime import datetime
try:
    import requests
    from dotenv import load_dotenv
except:
    print("pip install requests python-dotenv")
    sys.exit(1)
load_dotenv()
class Adapter:
    def __init__(self):
        os.chdir(Path(__file__).parent.parent)
        self.key = os.getenv("GROQ_API_KEY")
        if not self.key:
            print("ERROR: GROQ_API_KEY not in .env")
            sys.exit(1)
        self.ep = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "llama-3.3-70b-versatile"
        self.backups = {}
    def is_corrupted(self, text):
        if not isinstance(text, str): return True
        markers = ["ÃƒÆ'", "Ãâ€", "Ãƒâ€š", "ÃÂ", "Ãâ"]
        return any(marker in text for marker in markers)
    def escape_latex_ampersand(self, text):
        if not isinstance(text, str):
            return text
        # Escape common LaTeX special characters
        chars = {
            "&": r"\&",
            "%": r"\%",
            "$": r"\$",
            "#": r"\#",
            "_": r"\_",
            "{": r"\{",
            "}": r"\}",
            "~": r"\textasciitilde{}",
            "^": r"\textasciicircum{}",
            "\\": r"\textbackslash{}"
        }
        # Use regex to replace to avoid double escaping if run multiple times?
        # A simple replacement loop is risky if order matters or if already escaped.
        # Check for already escaped chars is hard. 
        # Assuming input is raw text from LLM.
        
        # But wait, sometimes we pass already escaped text?
        # The script is run repeatedly. If text in file is already "R\&D", 
        # escaping it again gives "R\\&D". 
        # We need to be careful.
        
        # Strategy: Only escape if not preceded by backslash.
        # But doing this for all chars is complex with regex.
        
        # Simpler approach for this specific context (LLM output):
        # We can assume LLM outputs raw text mostly.
        # But if we read from file, it might be escaped.
        
        # Let's handle at least the most dangerous ones that cause hangs/errors.
        # & % $ # _
        
        # Fix for "R&D" -> "R\&D"
        text = re.sub(r"(?<!\\)&", r"\\&", text)
        text = re.sub(r"(?<!\\)%", r"\%", text)
        text = re.sub(r"(?<!\\)\$", r"\$", text)
        text = re.sub(r"(?<!\\)#", r"\#", text)
        text = re.sub(r"(?<!\\)_", r"\_", text)
        
        return text
    def cleanup_artifacts(self, verbose=True):
        cleaned = 0
        extensions = [
            "cv.aux", "cv.log", "cv.out", "cv.toc", "cv.bbl", "cv.blg", 
            "cv.fls", "cv.fdb_latexmk", "cv.synctex.gz", "cv.run.xml", "cv.bcf"
        ]
        
        files_to_remove = set(extensions)
        for f in os.listdir("."):
            if f.endswith("-blx.bib") or f.endswith(".synctex.gz") or f.endswith(".upa"):
                files_to_remove.add(f)

        for fname in files_to_remove:
            fpath = Path(fname)
            if fpath.exists():
                try:
                    if verbose: print(f"    Removing {fname}...", end=" ")
                    fpath.unlink()
                    cleaned += 1
                    if verbose: print("OK")
                except Exception as e1:
                    # Retry
                    try:
                        time.sleep(1)
                        if fpath.exists():
                            fpath.unlink()
                        cleaned += 1
                        if verbose: print("OK (retry)")
                    except Exception as e2:
                        if verbose: print(f"Failed: {e2}")
        return cleaned
    def call(self, s, u, t=300):
        try:
            h = {"Authorization": f"Bearer {self.key}", "Content-Type": "application/json"}
            p = {"model": self.model, "messages": [{"role": "system", "content": s}, {"role": "user", "content": u}], "temperature": 0.6, "max_tokens": t}
            r = requests.post(self.ep, json=p, headers=h, timeout=30)
            data = r.json()
            return data["choices"][0]["message"]["content"] if "choices" in data else None
        except:
            return None
    def backup(self):
        for f in ["sections/section_headline.tex", "sections/section_competences.tex", "sections/section_experience_short.tex", "cv.tex"]:
            if Path(f).exists():
                try:
                    with open(f, encoding="utf-8") as file:
                        self.backups[f] = file.read()
                except:
                    pass
    def restore(self):
        for fpath, content in self.backups.items():
            try:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
            except:
                pass
    def extract_job_info(self, offer_text):
        """Extract job title, company, and skills dynamically using Groq API with corruption protection."""
        try:
            # Step 1: Extract basic job title from first lines (fallback)
            lines = offer_text.strip().split('\n')
            first_line = lines[0].strip() if lines else "Position"
            
            # Step 2: Use Groq to intelligently extract job info
            extraction_prompt = f"""Analyze this job offer and extract:
1. Job title (max 60 chars)
2. Company name (max 40 chars, or 'Unknown' if not found)
3. Top 5 key technical skills

Format your response EXACTLY as:
TITLE: [title]
COMPANY: [company]
SKILLS: [skill1, skill2, skill3, skill4, skill5]

Job offer excerpt:
{offer_text[:1500]}"""
            
            result = self.call(
                s="You are a job offer analyzer. Extract structured information accurately.",
                u=extraction_prompt,
                t=150
            )
            
            if not result or self.is_corrupted(result):
                # Fallback to basic extraction
                return first_line[:80], "Company", []
            
            # Step 3: Parse the response with corruption checks
            title = "Position"
            company = "Company"
            skills = []
            
            for line in result.split('\n'):
                line = line.strip()
                if not line:
                    continue
                    
                if line.startswith("TITLE:"):
                    extracted = line.replace("TITLE:", "").strip()
                    if not self.is_corrupted(extracted) and len(extracted) > 3:
                        title = extracted[:80]
                elif line.startswith("COMPANY:"):
                    extracted = line.replace("COMPANY:", "").strip()
                    if not self.is_corrupted(extracted) and len(extracted) > 2:
                        company = extracted[:50]
                elif line.startswith("SKILLS:"):
                    skills_str = line.replace("SKILLS:", "").strip().replace("[", "").replace("]", "")
                    if not self.is_corrupted(skills_str):
                        # Parse comma-separated skills
                        raw_skills = [s.strip() for s in skills_str.split(',') if s.strip()]
                        skills = [s for s in raw_skills if not self.is_corrupted(s)][:5]
            
            # Validate and return
            if not title or self.is_corrupted(title):
                title = first_line[:80]
            if not company or self.is_corrupted(company):
                company = "Company"
            
            return title, company, skills
        except Exception as e:
            print(f"    extract_job_info error: {e}")
            return "Position", "Company", []
    
    def extract_keywords(self, offer_text):
        """Extract ALL keywords from job offer: action verbs, technologies, soft skills, certifications."""
        try:
            extraction_prompt = f"""Analyze this job offer and extract keywords in these categories:
1. ACTION VERBS (pilote, conçoit, optimise, développe...)
2. TECHNICAL SKILLS (Python, Docker, CI/CD, Machine Learning...)
3. SOFT SKILLS (autonomie, rigueur, leadership, communication...)
4. CERTIFICATIONS (PMP, Scrum Master, AWS...)
5. METHODOLOGIES (Agile, DevOps, LEAN...)

Format EXACTLY as:
VERBS: [verb1, verb2, verb3]
TECH: [tech1, tech2, tech3]
SOFT: [soft1, soft2, soft3]
CERTS: [cert1, cert2]
METHODS: [method1, method2]

IMPORTANT:
- Return ONLY keywords, NO sentences or explanations.
- If a category is empty, return empty brackets [].
- Keywords must be short (1-3 words max).

Job offer:
{offer_text[:2000]}"""
            
            result = self.call(
                s="You are a keyword extraction expert for ATS optimization.",
                u=extraction_prompt,
                t=600  # Increased token limit
            )
            
            # Simple retry mechanism if result is empty or corrupted
            if not result or self.is_corrupted(result):
                print("    Retrying keyword extraction...")
                result = self.call(
                    s="You are a keyword extraction expert.",
                    u=extraction_prompt,
                    t=600
                )
            
            if not result or self.is_corrupted(result):
                # Fallback keywords if extraction fails completely
                print("    Extraction failed. Using fallback keywords from text analysis.")
                words = offer_text.lower().replace(',', ' ').replace('.', ' ').split()
                # Simple frequency analysis for fallback
                common_tech = ["python", "java", "c++", "javascript", "react", "angular", "node", "aws", "azure", "docker", "kubernetes", "sql", "nosql", "git", "linux", "matlab", "simulink"]
                found_tech = [w for w in common_tech if w in words]
                return {"verbs": [], "tech": list(set(found_tech)), "soft": [], "certs": [], "methods": []}
            
            keywords = {"verbs": [], "tech": [], "soft": [], "certs": [], "methods": []}
            
            def clean_keywords(k_str):
                if not k_str or self.is_corrupted(k_str): return []
                # Split by comma
                raw = [k.strip() for k in k_str.split(',') if k.strip()]
                # Filter out long sentences or invalid keywords
                cleaned = []
                for k in raw:
                    # Reject if too long (> 30 chars) or contains "..." or looks like a sentence
                    if len(k) > 30 or "..." in k or k.count(' ') > 3:
                        continue
                    cleaned.append(k)
                return cleaned

            for line in result.split('\n'):
                line = line.strip()
                if not line:
                    continue
                
                if line.startswith("VERBS:"):
                    verbs_str = line.replace("VERBS:", "").strip().replace("[", "").replace("]", "")
                    keywords["verbs"] = clean_keywords(verbs_str)[:15]  # Increased limit
                elif line.startswith("TECH:"):
                    tech_str = line.replace("TECH:", "").strip().replace("[", "").replace("]", "")
                    keywords["tech"] = clean_keywords(tech_str)[:20]    # Increased limit
                elif line.startswith("SOFT:"):
                    soft_str = line.replace("SOFT:", "").strip().replace("[", "").replace("]", "")
                    keywords["soft"] = clean_keywords(soft_str)[:10]    # Increased limit
                elif line.startswith("CERTS:"):
                    certs_str = line.replace("CERTS:", "").strip().replace("[", "").replace("]", "")
                    keywords["certs"] = clean_keywords(certs_str)[:5]
                elif line.startswith("METHODS:"):
                    methods_str = line.replace("METHODS:", "").strip().replace("[", "").replace("]", "")
                    keywords["methods"] = clean_keywords(methods_str)[:10]  # Increased limit
            
            return keywords
        except Exception as e:
            print(f"    extract_keywords error: {e}")
            return {"verbs": [], "tech": [], "soft": [], "certs": [], "methods": []}
    
    def calculate_match_score(self, keywords):
        """Calculate matching score (0-100%) between CV and job offer keywords."""
        try:
            cv_content = ""
            for f in ["sections/section_headline.tex", "sections/section_experience_short.tex", "sections/section_competences.tex"]:
                try:
                    with open(f, encoding="utf-8") as file:
                        cv_content += file.read() + "\n"
                except: pass

            cv_lower = cv_content.lower()
            total_keywords = 0
            found_keywords = 0
            
            # Count all keywords
            for category, kw_list in keywords.items():
                for kw in kw_list:
                    if len(kw) < 2: continue
                    total_keywords += 1
                    # Check if keyword appears in CV (case insensitive)
                    if kw.lower() in cv_lower:
                        found_keywords += 1
            
            if total_keywords == 0:
                return 0.0
            
            score = (found_keywords / total_keywords) * 100
            return round(score, 1)
        except:
            return 0.0
    
    def rewrite_competences(self, keywords):
        """Inject missing keywords into section_competences.tex securely by rebuilding the table."""
        try:
            comp_file = "sections/section_competences.tex"
            if not Path(comp_file).exists():
                return False
            
            with open(comp_file, "r", encoding="utf-8") as f:
                original_content = f.read()

            # Construct keywords string
            all_keywords = []
            for cat, kws in keywords.items():
                if kws:
                    all_keywords.extend(kws)
            keywords_str = ", ".join(all_keywords[:30]) # Top 30 keywords

            # Change prompt to ask for STRUCTURED DATA, not LaTeX code
            prompt = f"""Tu es un expert en recrutement technique. Analyse les compétences actuelles du candidat et les mots-clés de l'offre.
Ta mission : Fusionner intelligemment les deux listes pour créer une nouvelle liste de compétences optimisée.

CONTENU ACTUEL (Format LaTeX) :
{original_content}

MOTS-CLÉS À AJOUTER ABSOLUMENT (s'ils manquent) :
{keywords_str}

CONSIGNES STRICTES DE FORMAT DE SORTIE :
1. Renvoie UNIQUEMENT une liste ligne par ligne.
2. Chaque ligne doit suivre strictement ce format : "NOM_CATEGORIE : compétence1, compétence2, compétence3..."
3. UTILISE CES CATÉGORIES (adapte si nécessaire) : Langages, Modélisation & Simulation, Optimisation, DevOps, Cloud & Data, Data Analytics, CAO, Management, Autres.
4. Mets en PREMIER les compétences les plus demandées dans l'offre.
5. CRITIQUE : Chaque ligne ne doit pas dépasser 85 caractères. Sélectionne uniquement les 4-6 compétences les plus impactantes par catégorie pour que ça tienne sur UNE SEULE LIGNE.
6. PAS DE LATEX, PAS DE MARKDOWN, JUSTE DU TEXTE BRUT.
"""

            result = self.call("Expert Recrutement", prompt, 800)
            
            if not result or self.is_corrupted(result):
                return False
            
            # Clean up result
            lines = result.strip().split('\n')
            
            # Rebuild LaTeX Table safely in Python to avoid layout issues
            # Use top-aligned columns (p) instead of middle-aligned (m/R) for better multi-line behavior
            latex_header = (
                "\\sectionTitle{COMPÉTENCES}{\\faTasks}\n"
                "\\renewcommand{\\arraystretch}{1.1}\n"
                "\t\\begin{tabular}{>{}r>{}p{13cm}}\n"
            )
            latex_footer = "\t\\end{tabular}\n"
            latex_body = ""
            
            has_content = False
            for line in lines:
                line = line.strip()
                if not line or ":" not in line:
                    continue
                
                parts = line.split(":", 1)
                category = parts[0].strip().replace("*", "") # Remove markdown bold if present
                skills = parts[1].strip()
                
                # Escape LaTeX special characters
                category = self.escape_latex_ampersand(category)
                skills = self.escape_latex_ampersand(skills)
                
                # Format checks
                if len(category) < 2 or len(skills) < 3:
                     continue
                
                # Force single line (approx 75 chars max for 11.5cm in small font)
                if len(skills) > 75:
                     skill_parts = [s.strip() for s in skills.split(',')]
                     fitted_skills = []
                     current_length = 0
                     for s in skill_parts:
                         if current_length + len(s) + 2 > 75:
                             break
                         fitted_skills.append(s)
                         current_length += len(s) + 2
                     skills = ", ".join(fitted_skills)

                latex_body += f"\t    \\textbf{{{category}:}} & {skills}\\\\\n"
                has_content = True
            
            if not has_content:
                return False
                
            final_latex = latex_header + latex_body + latex_footer
            
            with open(comp_file, "w", encoding="utf-8") as f:
                f.write(final_latex)
            
            return True
        except Exception as e:
            print(f"    rewrite_competences error: {e}")
            return False

    def inject_keywords_in_experiences(self, keywords, job_title):
        """Enrich experience keywords section with keywords from job offer."""
        try:
            exp_file = "sections/section_experience_short.tex"
            if not Path(exp_file).exists():
                return False
            
            with open(exp_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            # Combine relevant keywords for enrichment (Tech and Methods are best for the stack line)
            keywords_to_inject = []
            keywords_to_inject.extend(keywords.get("tech", [])[:10])  # Increased from 6
            keywords_to_inject.extend(keywords.get("methods", [])[:5]) # Increased from 3
            
            # Filter out empty or invalid keywords
            keywords_to_inject = [kw for kw in keywords_to_inject if kw and isinstance(kw, str) and len(kw) > 2]
            
            if not keywords_to_inject:
                return False
            
            # Track used keywords to avoid repetition
            used_keywords = set()

            experience_count = 0
            in_itemize = False
            modified = False
            expecting_keywords = False
            
            for i, line in enumerate(lines):
                # Detect start of an experience
                if "\\experience" in line:
                    experience_count += 1
                    in_itemize = False
                    expecting_keywords = False
                
                # Only process first 2 experiences
                if experience_count > 2:
                    break
                
                # Detect end of itemize to find the keywords line following it
                if "\\end{itemize}" in line:
                    expecting_keywords = True
                    continue

                # If we are expecting keywords and find a line starting with {, it's the keywords line
                if expecting_keywords and line.strip().startswith("{"):
                    # This is the keywords line: {Key1, Key2, ...}
                    content = line.strip()
                    
                    # Remove enclosing braces for processing
                    if content.startswith("{") and content.endswith("}"):
                        inner_content = content[1:-1]
                        current_keywords = [k.strip() for k in inner_content.split(',') if k.strip()]
                        
                        # Add new keywords if not present
                        added_count = 0
                        for kw in keywords_to_inject:
                            escaped_kw = self.escape_latex_ampersand(kw)
                            # Check if keyword is already present (case insensitive)
                            if not any(k.lower() == escaped_kw.lower() for k in current_keywords) and escaped_kw not in used_keywords:
                                current_keywords.append(escaped_kw)
                                used_keywords.add(escaped_kw)
                                added_count += 1
                                if added_count >= 5: # Increased from 3 to 5 keywords per experience
                                    break
                        
                        # FORCE SINGLE LINE (max ~95 chars for standard layout width)
                        final_keywords_list = []
                        current_len = 0
                        # Prioritize keeping keywords, but truncate to fit single line
                        for kw in current_keywords:
                            if current_len + len(kw) + 2 > 95:
                                break
                            final_keywords_list.append(kw)
                            current_len += len(kw) + 2
                            
                        # Reconstruct the line
                        new_content = "    {" + ", ".join(final_keywords_list) + "}\n"
                        if new_content != lines[i]:
                            lines[i] = new_content
                            modified = True
                    
                    expecting_keywords = False # Done for this experience

            if not modified:
                return False
            
            # Write enriched content
            with open(exp_file, "w", encoding="utf-8") as f:
                f.writelines(lines)
            
            return True
        except Exception as e:
            print(f"    inject_keywords_in_experiences error: {e}")
            return False
    
    def optimize_for_ats(self, keywords, job_title):
        """Optimize CV for ATS: inject keywords, validate formatting."""
        try:
            # Rewrites competences table 
            comp_success = self.rewrite_competences(keywords)

            # Inject keywords into experiences
            success = self.inject_keywords_in_experiences(keywords, job_title)
            
            return success or comp_success
        except Exception as e:
            print(f"    optimize_for_ats error: {e}")
            return False
    
    def reduce_to_one_page(self):
        """Reduce CV to 1 page: keep all experiences but detail only those > 2 years, others show only keywords."""
        try:
            exp_file = "sections/section_experience_short.tex"
            if not Path(exp_file).exists():
                return False
            
            with open(exp_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Define experiences with their durations (manually determined from dates)
            # Schneider: Dec 2022 - now = 3 years ✓
            # TRISKELL: Feb 2022 - Nov 2022 = 10 months ✗
            # Carmat: Dec 2021 - Jan 2022 = 1 month ✗  
            # PSG-DOVER: Jan 2019 - Nov 2021 = 2y 10m ✓
            # LUSAC: Dec 2015 - Nov 2018 = 3 years ✓
            # Liebherr: Apr 2015 - Sep 2015 = 5 months ✗
            # ARIANESPACE: Dec 2014 - Mar 2015 = 3 months ✗
            # Aperam: Feb 2014 - Jul 2014 = 5 months ✗
            
            short_positions = ["ARIANESPACE", "APERAM"]
            
            lines = content.split('\n')
            new_lines = []
            in_short_position = False
            in_itemize = False
            items_count = 0
            
            for line in lines:
                # Detect if we're entering a new experience
                if "\\experience" in line:
                    in_short_position = False
                
                # Check if this line contains a short position company
                for company in short_positions:
                    if company in line:
                        in_short_position = True
                        break
                
                # Handle itemize block
                if "\\begin{itemize}" in line:
                    in_itemize = True
                    items_count = 0
                    new_lines.append(line)
                    continue
                
                if "\\end{itemize}" in line:
                    in_itemize = False
                    new_lines.append(line)
                    continue
                
                if in_itemize:
                    if "\\item" in line:
                        items_count += 1
                        if in_short_position:
                            if items_count <= 3: # Keep only first 3 items for short positions
                                new_lines.append(line)
                        else:
                            new_lines.append(line) # Keep all items for long positions
                    else:
                        # Keep non-item lines only if we haven't exceeded the limit for short positions
                        if in_short_position and items_count > 3:
                            continue
                        new_lines.append(line)
                else:
                    new_lines.append(line)
            
            print(f"  OK - Detailed only 2+ years positions (others reduced to 3 items)")

            # Write reduced content
            with open(exp_file, "w", encoding="utf-8") as f:
                f.write('\n'.join(new_lines))
            
            return True
        except Exception as e:
            print(f"    reduce_to_one_page error: {e}")
            return False
    
    def optimize_tagline(self, job_title, key_skills, detailed_keywords=None):
        try:
            skills_str = ", ".join(key_skills) if key_skills else "required"
            context = ""
            if detailed_keywords and detailed_keywords.get('tech'):
                context = f"Basé sur ces technos clés: {', '.join(detailed_keywords['tech'][:3])}."
                
            prompt = f"Pour un poste de {job_title}, propose un sous-titre de 4-5 mots maximum en français. Format : 'Expertise1 & Expertise2'. Doit être cohérent avec ces compétences : {skills_str}. {context} Réponds UNIQUEMENT le sous-titre."
            result = self.call(prompt, job_title, 100)
            if result:
                result = result.strip().replace("`", "").strip()
                if len(result) > 50: result = result[:50].strip()
                return result if len(result) > 5 else None
        except:
            pass
        return None
    def update_tagline_in_cv(self, new_tagline_part):
        try:
            with open("cv.tex", "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            # Find and replace the tagline line directly
            new_tagline_part = self.escape_latex_ampersand(new_tagline_part)
            #new_tagline_part = "Modélisation & Optimisation Avancée"  # Fixed tagline for French CV adaptation
            
            for i, line in enumerate(lines):
                if "\\tagline{" in line:
                    # Replace the entire line
                    lines[i] = f"\\tagline{{Ingénieur R\\&D Senior | {new_tagline_part}}}\n"
                    break
            
            with open("cv.tex", "w", encoding="utf-8") as f:
                f.writelines(lines)
            
            return True
        except Exception as e:
            print(f"    Error updating tagline: {e}")
        return False
    def optimize_headline(self, original_text, job_title, company, key_skills, detailed_keywords=None):
        try:
            skills_str = ", ".join(key_skills) if key_skills else "skills"
            
            # Construire une liste enrichie de mots-clés si disponible
            context_keywords = ""
            if detailed_keywords:
                tech = ", ".join(detailed_keywords.get('tech', [])[:8])
                soft = ", ".join(detailed_keywords.get('soft', [])[:5])
                methods = ", ".join(detailed_keywords.get('methods', [])[:3])
                context_keywords = f"""
            MOTS-CLÉS DU POSTE À INCLURE ABSOLUMENT (si pertinent) :
            - Tech : {tech}
            - Soft Skills : {soft}
            - Méthodologies : {methods}
            """

            prompt = f"""Agis comme un expert en recrutement sénior. Rédige un résumé professionnel (headline) percutant et sur-mesure pour un poste de {job_title} chez {company}.
            
            LE PROFIL DU CANDIDAT (Ne pas inventer d'informations non présentes ici) :
            "{original_text}"

            COMPÉTENCES CLÉS PRIORITAIRES :
            {skills_str}
            {context_keywords}

            INSTRUCTIONS :
            1. OBJECTIF : Rédiger un profil (Executive Summary) structuré, riche et détaillé (environ 650 caractères), qui justifie l'adéquation au poste.
            2. INTERDIT ABSOLU :
               - Formule "je maîtrise X, Y, Z" ou "expert en X, Y, Z".
               - Répétition de mots (ex: "gestion" deux fois, "système" deux fois).
               - Majuscules pour les noms communs.
            3. TRADUCTION OBLIGATOIRE : Traduis TOUS les termes métiers en Français avec des synonymes variés (ex: "Quotation" -> "Elaboration de devis", "Order Management" -> "Suivi des commandes", "Parts Management" -> "Logistique de pièces").
            4. STRUCTURE IMPOSÉE (3 phrases complètes) :
               - Phrase 1 (Accroche) : "Fort de 10 ans d'expérience en [Domaine], j'apporte une expertise en [Compétence A] pour optimiser [Objectif du poste]."
               - Phrase 2 (Technique - DOIT ÊTRE DÉTAILLÉE) : "Mon savoir-faire en [Outils/Produits Spécifiques de l'offre] me permet de [Résultat Concret : réduire les délais, garantir la qualité, etc.]."
               - Phrase 3 (Méthode/Soft) : "Alliant [Qualité Humaine] et [Méthodologie], je m'implique dans la réussite de vos projets [Type de projet]."
            5. FORMATAGE : Mets en GRAS les 3-4 mots-clés les plus importants (ex: \\textbf{{Python}}).
            6. Limite à 650 caractères. Sois précis et technique.
            """
            
            result = self.call("Tu es un expert en rédaction de CV et en recrutement.", prompt, 750)
            
            if not result:
                print("    Error: LLM returned no result")
                return None
                
            if result:
                result = result.strip().replace("`", "").strip()
                result = " ".join(result.split())
                result = self.escape_latex_ampersand(result)
                
                # Convert markdown bold to latex bold if LLM messes up
                result = re.sub(r"\*\*(.*?)\*\*", r"\\textbf{\1}", result)
                
                # Corruption protection: fix "Ingénieur RD" → "Ingénieur R&D"
                result = re.sub(r"ingénierie\s+R&D", "ingénierie R\\&D", result, flags=re.IGNORECASE)
                result = re.sub(r"Ingénieur\s+R&D", "Ingénieur R\\&D", result, flags=re.IGNORECASE)
                
                if self.is_corrupted(result):
                    print(f"    Error: Result corrupted: {result[:50]}...")
                    return None
                
                if len(result) < 100: # Lowered minimum length requirement
                    print(f"    Error: Result too short ({len(result)} chars)")
                    return None
                 
                # Smart truncation: keep full sentences
                if len(result) > 550:
                    truncated = result[:550]
                    last_period = truncated.rfind(".")
                    if last_period > 300:
                        result = truncated[:last_period + 1].strip()
                    else:
                        result = result[:500].strip() + "."
                
                return result
        except:
            pass
        return None
    def run(self):
        print("\n" + "="*80)
        print("CV ADAPTER v11.0 - 1-PAGE CV OPTIMIZATION")
        print("="*80 + "\n")
        pdf_path = None
        try:
            print("STEP 1: Backup files...")
            self.backup()
            print("  OK\n")
            print("STEP 2: Load offer...")
            with open("offers/offre.txt", encoding="utf-8") as f:
                offer = f.read()
            print(f"  OK ({len(offer)} chars)\n")
            print("STEP 3: Analyze job...")
            job_title, company, key_skills = self.extract_job_info(offer)
            print(f"  Title: {job_title}")
            print(f"  Company: {company}")
            print(f"  Skills: {', '.join(key_skills)}\n")
            
            print("STEP 3b: Extract keywords for ATS...")
            keywords = self.extract_keywords(offer)
            total_kw = sum(len(v) for v in keywords.values())
            print(f"  Extracted {total_kw} keywords:")
            if keywords["tech"]:
                print(f"    Tech: {', '.join(keywords['tech'][:5])}{'...' if len(keywords['tech']) > 5 else ''}")
            if keywords["methods"]:
                print(f"    Methods: {', '.join(keywords['methods'][:3])}{'...' if len(keywords['methods']) > 3 else ''}")
            if keywords["verbs"]:
                print(f"    Verbs: {', '.join(keywords['verbs'][:3])}{'...' if len(keywords['verbs']) > 3 else ''}")
            print("")
            
            print("STEP 3c: Inject keywords in experiences...")
            injection_success = self.optimize_for_ats(keywords, job_title)
            if injection_success:
                print("  OK - Experiences enriched\n")
            else:
                print("  Skipped - No keywords to inject\n")
            
            print("STEP 3d: Reduce to 2 pages format...")
            reduce_success = self.reduce_to_one_page()
            if reduce_success:
                print("  OK - Kept all experiences, detailed only 2+ years positions (others reduced to 3 items)\n")
            else:
                print("  Warning - Could not optimize for 2 pages\n")
            print("STEP 4: Optimize headline...")
            with open("sections/section_headline.tex", encoding="utf-8") as f:
                hl_orig = f.read()
            m = re.search(r"\\par\{(.*?)\}", hl_orig, re.DOTALL)
            hl_text = m.group(1).strip() if m else hl_orig
            # Passe les mots-clés détaillés à la fonction (keywords est déjà extrait à l'étape 3b)
            optimized_hl = self.optimize_headline(hl_text, job_title, company, key_skills, detailed_keywords=keywords)
            if optimized_hl:
                print(f"  Generated Headline: {optimized_hl}")
                with open("sections/section_headline.tex", "w", encoding="utf-8") as f:
                    f.write(f"\\par{{\n{optimized_hl}\n}}\n\\newline\n")
            print("")
            print("STEP 5: Optimize tagline...")
            tagline_adapted = self.optimize_tagline(job_title, key_skills, detailed_keywords=keywords)
            if tagline_adapted:
                print(f"  Tagline: {tagline_adapted}")
                if self.update_tagline_in_cv(tagline_adapted):
                    print(f"  Updated\n")
                else:
                    print(f"  Update failed\n")
            print("STEP 6: Compile PDF...")
            result = subprocess.run(["lualatex", "-interaction=nonstopmode", "cv.tex"], capture_output=True, timeout=60, text=True)
            
            # Check if PDF was created
            if not Path("cv.pdf").exists():
                print(f"  ERROR: PDF not created")
                print(f"  LaTeX exit code: {result.returncode}")
                if result.stderr:
                    print(f"  LaTeX stderr: {result.stderr[:500]}")
                # Print last lines of log file for debugging
                if Path("cv.log").exists():
                    with open("cv.log", "r", encoding="utf-8", errors="ignore") as log:
                        lines = log.readlines()
                        print(f"  Last log lines: {''.join(lines[-10:])}")
                return False
            
            time.sleep(0.5)
            print("  OK\n")
            print("STEP 7: Cleanup...")
            self.cleanup_artifacts()
            print("  OK\n")
            print("STEP 8: Process PDF...")
            if Path("cv.pdf").exists():
                ts = datetime.now().strftime("%Y%m%d_%H%M%S")
                pdf_path = f"output/CV_ROMDHANE_Jaouher.pdf"
                Path("output").mkdir(exist_ok=True)
                
                # Close any file handles and retry with delay if needed
                time.sleep(1)
                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        if Path(pdf_path).exists():
                            Path(pdf_path).unlink()
                        shutil.move("cv.pdf", pdf_path)
                        if Path("cv.pdf").exists():
                             try: Path("cv.pdf").unlink()
                             except: pass
                        print(f"  OK: {pdf_path}\n")
                        break
                    except PermissionError:
                        if attempt < max_retries - 1:
                            time.sleep(2)
                        else:
                            print(f"  Warning: Could not move PDF (file in use). Please close the PDF viewer.\n")
                            pdf_path = "cv.pdf"
            
            # Calculate matching score BEFORE restoring files
            print("STEP 9: Calculate matching score...")
            try:
                match_score = self.calculate_match_score(keywords)
                print(f"  Matching score: {match_score}%\n")
            except Exception as e:
                print(f"  Could not calculate score: {e}\n")
                match_score = 0.0
            
            print("STEP 10: Restore files...")
            self.restore()
            print("  OK")
            
            # Final cleanup attempt in case restoration triggered something or files appeared late
            # Check if artifacts reappeared
            if any(Path(f).exists() for f in ["cv.aux", "cv.log", "cv.synctex.gz", "cv.pdf"]):
                 print("  Performing final cleanup...")
                 self.cleanup_artifacts(verbose=False)
                 if Path("cv.pdf").exists():
                     try: Path("cv.pdf").unlink()
                     except: pass
            print("")

            print("="*80)
            print(f"MATCHING SCORE: {match_score}%")
            print("="*80 + "\n")
            print("="*80)
            print("SUCCESS - CV ADAPTED")
            print("="*80 + "\n")
            return True
        except Exception as e:
            print(f"ERROR: {e}\n")
            self.restore()
            return False
if __name__ == "__main__":
    adapter = Adapter()
    adapter.run()
