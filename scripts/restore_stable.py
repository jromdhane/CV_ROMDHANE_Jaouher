#!/usr/bin/env python3#!/usr/bin/env python3

"""Restore stable CV versions - all 8 experiences with compact spacing""""""Restore stable CV versions - all 8 experiences with compact spacing"""

import os, sysimport os, sys

from pathlib import Pathfrom pathlib import Path



os.chdir(Path(__file__).parent.parent)os.chdir(Path(__file__).parent.parent)



# CV main file - COMPACT MODE enabled for optimal 2-page layout# CV main file - COMPACT MODE enabled for optimal 2-page layout

cv_main = r"""\documentclass[localFont,alternative,compact]{awesome-source-cv}cv_main = r"""\documentclass[localFont,alternative,compact]{awesome-source-cv}



\name{Jaouher}{ROMDHANE}\name{Jaouher}{ROMDHANE}

\photo{3.3 cm}{photos/jaouher}\photo{3.3 cm}{photos/jaouher}

\tagline{Ingénieur R\&D Senior | Model-Based Design \& DevOps Expert}\tagline{Ingénieur R\&D Senior | Model-Based Design \& DevOps Expert}

\socialinfo{\socialinfo{

	\linkedin{jaouher-romdhane}\\	\linkedin{jaouher-romdhane}\\

	\smartphone{+33.6.10.59.22.70}\\	\smartphone{+33.6.10.59.22.70}\\

	\email{romdhanejaouher@gmail.com}\\	\email{romdhanejaouher@gmail.com}\\

	\address{Île-de-France, France}\\	\address{Île-de-France, France}\\

	\infos{34 ans, Français}	\infos{34 ans, Français}

}}

%------------------------------------------%------------------------------------------

\begin{document}\begin{document}



\makecvheader\makecvheader



%--------------------SECTIONS-----------------------------------%--------------------SECTIONS-----------------------------------

\input{sections/section_headline}\input{sections/section_headline}

\input{sections/section_competences}				% Section compétence\input{sections/section_competences}				% Section compétence

\input{sections/section_experience_short}			% Section expérience\input{sections/section_experience_short}			% Section expérience

\input{sections/section_scolarite}					% Section scolarité\input{sections/section_scolarite}					% Section scolarité

\input{sections/section_certifications}				% Section certifications\input{sections/section_certifications}				% Section certifications

\input{sections/section_langues}					% Section langues\input{sections/section_langues}					% Section langues

%\input{section_interets}					        % Section intérêts%\input{section_interets}					        % Section intérêts

\input{sections/section_references} 				% Section références\input{sections/section_references} 				% Section références



\end{document}\end{document}

""""""



# Experience section - ALL 8 POSITIONS WITH FULL DETAILS FOR 2-PAGE LAYOUT# Headline content - CLEAN AND VERIFIED

experience = r"""\sectionTitle{EXPÉRIENCE PROFESSIONNELLE}{\faSuitcase}headline = r"""\par{

\begin{experiences}Ingénieur modélisation de procédé expérimenté (10 ans d'expérience), spécialisé en physique et chimie de procédés complexes, modélisation du procédé, sûreté et exploitation. Je conçois et optimise des systèmes énergétiques avec expertise en Data Science, Machine Learning, Model-Based Design et modélisation de la physique pour améliorer la performance et la fiabilité des équipements procédé. Certifié PMP®, Scrum Master, je pilote des projets agiles avec intégration de jumeaux numériques pour soutenir l'exploitation et la sûreté.

  \experience}

    {À ce jour}   {Ingénieur R\&D Senior}{Schneider Electric}{Pacy-sur-Eure, France}\newline

    {Décembre 2022} {"""

      \begin{itemize}

        \item Pilotage Agile et coaching d'équipes# Experience section - ALL 8 POSITIONS WITH FULL DETAILS FOR 2-PAGE LAYOUT

        \item Conception de pipelines de données complexesexperience = r"""\sectionTitle{EXPÉRIENCE PROFESSIONNELLE}{\faSuitcase}

        \item Modélisation MBD et optimisation de composants\begin{experiences}

        \item DevOps : pipelines CI/CD, automatisation tests  \experience

      \end{itemize}    {À ce jour}   {Ingénieur R\&D Senior}{Schneider Electric}{Pacy-sur-Eure, France}

    }    {Décembre 2022} {

    {MATLAB, Simulink, Python, Git, TensorFlow, Scikit-learn, Scrum, Thermodynamique}      \begin{itemize}

  \emptySeparator        \item Pilotage Agile et coaching d'équipes

        \item Conception de pipelines de données complexes

  \experience        \item Modélisation MBD et optimisation de composants

    {Novembre 2022}   {Ingénieur R\&D Senior}{TRISKELL-CONSULTING}{Puteaux, France}        \item DevOps : pipelines CI/CD, automatisation tests

    {Février 2022} {      \end{itemize}

      \begin{itemize}    }

        \item Modélisation multiphysique (MBD)    {MATLAB, Simulink, Python, Git, TensorFlow, Scikit-learn, Scrum, Thermodynamique}

        \item Optimisation du dimensionnement et du contrôle  \emptySeparator

        \item Conception de modèles prédictifs et traitement de données

        \item Intégration de critères de performance énergétique  \experience

        \item Mise en œuvre de pratiques DevOps : pipelines CI/CD, automatisation des tests    {Novembre 2022}   {Ingénieur R\&D Senior}{TRISKELL-CONSULTING}{Puteaux, France}

      \end{itemize}    {Février 2022} {

    }      \begin{itemize}

    {MATLAB, Simulink, Python, Git, GitHub, TensorFlow, Scikit-learn, Thermodynamique, KUBERNETES, DOCKER}        \item Modélisation multiphysique (MBD)

  \emptySeparator        \item Optimisation du dimensionnement et du contrôle

        \item Conception de modèles prédictifs et traitement de données

  \experience        \item Intégration de critères de performance énergétique

    {Janvier 2022}   {Ingénieur R\&D Senior}{Carmat}{Vélizy-Villacoublay, France}        \item Mise en œuvre de pratiques DevOps : pipelines CI/CD, automatisation des tests

    {Décembre 2021} {      \end{itemize}

      \begin{itemize}    }

        \item Définition d'indicateurs techniques et physiologiques    {MATLAB, Simulink, Python, Git, GitHub, TensorFlow, Scikit-learn, Thermodynamique, KUBERNETES, DOCKER}

        \item Conception et maintenance de pipelines de données complexes  \emptySeparator

        \item Conception de modèles prédictifs et traitement de données

        \item Développement de tableaux de bord dynamiques  \experience

        \item Pilotage Agile et industrialisation    {Janvier 2022}   {Ingénieur R\&D Senior}{Carmat}{Vélizy-Villacoublay, France}

      \end{itemize}    {Décembre 2021} {

    }      \begin{itemize}

    {Python, Power BI, Tableau, GitHub Actions, TensorFlow, Scikit-learn, DevOps, SQL, Thermodynamique}        \item Définition d'indicateurs techniques et physiologiques

  \emptySeparator        \item Conception et maintenance de pipelines de données complexes

        \item Conception de modèles prédictifs et traitement de données

  \experience        \item Développement de tableaux de bord dynamiques

    {Novembre 2021}   {Ingénieur R\&D}{PSG-DOVER}{Auxerre, France}        \item Pilotage Agile et industrialisation

    {Janvier 2019} {      \end{itemize}

      \begin{itemize}    }

        \item Support technique produit et mise en production    {Python, Power BI, Tableau, GitHub Actions, TensorFlow, Scikit-learn, DevOps, SQL, Thermodynamique}

        \item Conception et maintenance de pipelines de données complexes  \emptySeparator

        \item Conception de modèles prédictifs et traitement de données

        \item Modélisation multiphysique et simulation  \experience

        \item Rédaction technique et veille sectorielle    {Novembre 2021}   {Ingénieur R\&D}{PSG-DOVER}{Auxerre, France}

      \end{itemize}    {Janvier 2019} {

    }      \begin{itemize}

    {MATLAB, Simulink, Python, CATIA v5, CAO, TensorFlow, Scikit-learn, Model-Based Design, Thermodynamique}        \item Support technique produit et mise en production

  \emptySeparator        \item Conception et maintenance de pipelines de données complexes

        \item Conception de modèles prédictifs et traitement de données

  \experience        \item Modélisation multiphysique et simulation

    {Décembre 2015}   {Ingénieur R\&D}{LUSAC}{Caen, France}        \item Rédaction technique et veille sectorielle

    {Décembre 2018} {      \end{itemize}

      \begin{itemize}    }

        \item Conception et validation expérimentale    {MATLAB, Simulink, Python, CATIA v5, CAO, TensorFlow, Scikit-learn, Model-Based Design, Thermodynamique}

        \item Suivi de projet et coordination des prestataires  \emptySeparator

        \item Conception de modèles prédictifs et modélisation multiphysique

        \item Développement de briques technologiques  \experience

        \item Veille technologique sur les systèmes énergétiques    {Décembre 2015}   {Ingénieur R\&D}{LUSAC}{Caen, France}

      \end{itemize}    {Décembre 2018} {

    }      \begin{itemize}

    {MATLAB, Simulink, Python, CATIA v5, CAO, TensorFlow, Scikit-learn, Thermodynamique, Hydrogène, Piles à combustible}        \item Conception et validation expérimentale

  \emptySeparator        \item Suivi de projet et coordination des prestataires

        \item Conception de modèles prédictifs et modélisation multiphysique

  \experience        \item Développement de briques technologiques

    {Septembre 2015}   {Ingénieur R\&D}{Liebherr Aerospace and Transportation}{Toulouse, France}        \item Veille technologique sur les systèmes énergétiques

    {Avril 2015} {      \end{itemize}

      \begin{itemize}    }

        \item Conception et validation expérimentale    {MATLAB, Simulink, Python, CATIA v5, CAO, TensorFlow, Scikit-learn, Thermodynamique, Hydrogène, Piles à combustible}

        \item Définition des scénarios de test  \emptySeparator

        \item Conception de modèles prédictifs

        \item Modélisation multiphysique et simulation  \experience

        \item Rédaction de documents techniques    {Septembre 2015}   {Ingénieur R\&D}{Liebherr Aerospace and Transportation}{Toulouse, France}

      \end{itemize}    {Avril 2015} {

    }      \begin{itemize}

    {VBA, Simulink, CATIA v5, Hydraulique, Thermodynamique, Transfert thermique, Model-Based Design, Simulation}        \item Conception et validation expérimentale

  \emptySeparator        \item Définition des scénarios de test

        \item Conception de modèles prédictifs

  \experience        \item Modélisation multiphysique et simulation

    {Mars 2015}   {Ingénieur R\&D}{ARIANESPACE}{Les Mureaux, France}        \item Rédaction de documents techniques

    {Décembre 2014} {      \end{itemize}

      \begin{itemize}    }

        \item Modélisation physique et analyse de trajectoire    {VBA, Simulink, CATIA v5, Hydraulique, Thermodynamique, Transfert thermique, Model-Based Design, Simulation}

        \item Conception de modèles prédictifs  \emptySeparator

        \item Modélisation multiphysique et simulation

        \item Développement de briques technologiques  \experience

        \item Rédaction de documents techniques    {Mars 2015}   {Ingénieur R\&D}{ARIANESPACE}{Les Mureaux, France}

      \end{itemize}    {Décembre 2014} {

    }      \begin{itemize}

    {Fortran, Thermodynamique, Programmation et algorithmique, Aérodynamique, Simulation numérique, Transfert thermique}        \item Modélisation physique et analyse de trajectoire

  \emptySeparator        \item Conception de modèles prédictifs

        \item Modélisation multiphysique et simulation

  \experience        \item Développement de briques technologiques

    {Juillet 2014}   {Ingénieur R\&D}{Aperam}{Gueugnon, France}        \item Rédaction de documents techniques

    {Février 2014} {      \end{itemize}

      \begin{itemize}    }

        \item Conception et dimensionnement de protecteurs industriels    {Fortran, Thermodynamique, Programmation et algorithmique, Aérodynamique, Simulation numérique, Transfert thermique}

        \item Réalisation de calculs et analyses pour la conformité réglementaire  \emptySeparator

        \item Modélisation multiphysique et simulation

        \item Développement de briques technologiques  \experience

        \item Rédaction de documents techniques    {Juillet 2014}   {Ingénieur R\&D}{Aperam}{Gueugnon, France}

      \end{itemize}    {Février 2014} {

    }      \begin{itemize}

    {VBA, Simulink, CATIA v5, Thermodynamique, Calcul de Structures, CAO, Systèmes hydrauliques}        \item Conception et dimensionnement de protecteurs industriels

  \emptySeparator        \item Réalisation de calculs et analyses pour la conformité réglementaire

\end{experiences}        \item Modélisation multiphysique et simulation

"""        \item Développement de briques technologiques

        \item Rédaction de documents techniques

print("\n" + "="*80)      \end{itemize}

print("CV RESTORATION - STABLE 2-PAGE VERSION")    }

print("="*80 + "\n")    {VBA, Simulink, CATIA v5, Thermodynamique, Calcul de Structures, CAO, Systèmes hydrauliques}

  \emptySeparator

try:\end{experiences}

    # Restore cv.tex with compact mode"""

    with open("cv.tex", "w", encoding="utf-8") as f:

        f.write(cv_main)# Competences section - COMPACT TABLEAU FORMAT (2 pages)

    print("✓ Restored: cv.tex (compact mode enabled)")competences = r"""\sectionTitle{COMPÉTENCES}{\faTasks}

\renewcommand{\arraystretch}{1.1}

    # Restore experience with all 8 positions

    with open("sections/section_experience_short.tex", "w", encoding="utf-8") as f:	\begin{tabular}{>{}r>{}p{13cm}} 

        f.write(experience)		\textbf{Modélisation:}  		&   Multiphysique, MBD, Simulation, MATLAB, Simulink, Aspen\\ 

    print("✓ Restored: sections/section_experience_short.tex (all 8 positions)")		\textbf{Développement:}               	&   Python, C, Scala, Shell, Git, GitHub\\ 

		\textbf{DevOps:}   &   CI/CD, GitHub Actions, Jenkins, Docker, Kubernetes, Linux, Terraform \\ 

    print("\n" + "="*80)		\textbf{Cloud \& Big Data:}	  		        &   AWS (Glue, S3, RDS, Lambda), GCP (BigQuery, Cloud Functions), Hadoop, Spark, Airflow \\

    print("✓ ALL FILES RESTORED TO STABLE 2-PAGE STATE")		\textbf{Data Analytics:}		&  Power BI, Tableau, TensorFlow, Scikit-learn, Machine Learning \\ 

    print("="*80 + "\n")        \textbf{CAO:}		                &  CATIA v5, Solidworks\\

        \textbf{Autres:}		            &  ETL, API, automatisation, NLP, modélisation de données, VBA, JIRA, Scrum, Agile, PMP, Thermodynamique, Hydraulique

except Exception as e:	\newline

    print(f"\n✗ ERROR: {e}\n")    \end{tabular}

    sys.exit(1)"""


print("\n" + "="*80)
print("CV RESTORATION - STABLE VERSION")
print("="*80 + "\n")

try:
    # Restore headline
    with open("sections/section_headline.tex", "w", encoding="utf-8") as f:
        f.write(headline)
    print("✓ Restored: sections/section_headline.tex")

    # Restore experience
    with open("sections/section_experience_short.tex", "w", encoding="utf-8") as f:
        f.write(experience)
    print("✓ Restored: sections/section_experience_short.tex")

    # Restore competences
    with open("sections/section_competences.tex", "w", encoding="utf-8") as f:
        f.write(competences)
    print("✓ Restored: sections/section_competences.tex")

    print("\n" + "="*80)
    print("✓ ALL FILES RESTORED TO STABLE STATE")
    print("="*80 + "\n")

except Exception as e:
    print(f"\n✗ ERROR: {e}\n")
    sys.exit(1)
