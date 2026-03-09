# Index de la Documentation

Vue d'ensemble de la structure des fichiers et de la documentation du projet.

## Fichiers Principaux

- **[README.md](README.md)** : Guide de démarrage et vue d'ensemble.
- **[CHANGELOG.md](CHANGELOG.md)** : Historique des versions et modifications.
- **[VERSION](VERSION)** : Fichier contenant la version actuelle du projet.

## Source LaTeX

- **`cv.tex`** : Le fichier source principal LaTeX qui assemble toutes les sections.
- **`awesome-source-cv.cls`** : La définition du style (classe) du CV.
- **`cv-blx.bib`** : Bibliographie (si utilisée).

## Sections du CV (`sections/`)

Les différentes parties du CV sont isolées pour faciliter la maintenance :

- `section_headline.tex` : En-tête (Nom, Titre, Contact).
- `section_competences.tex` : Liste des compétences techniques.
- `section_experience_short.tex` : Expériences professionnelles (format court/optimisé).
- `section_certifications.tex` : Certifications obtenues.
- `section_scolarite.tex` : Formation académique.
- `section_langues.tex` : Langues parlées.
- `section_references.tex` : Références professionnelles.

## Scripts & Automatisation (`scripts/`)

- **`adapt_cv.py`** : Le cerveau du projet. Il :
  1. Lit la dernière offre dans `offers/`.
  2. Appelle une API pour extraire les mots-clés.
  3. Injecte ces mots-clés dans les fichiers LaTeX.
  4. Compile le PDF.
  5. Vérifie le nombre de pages.
- **`restore_stable.py`** : Utilitaire pour restaurer une version stable des fichiers LaTeX en cas d'erreur.
- **`generate_interview_pdf.py`** : Script pour préparer des documents d'entretien.

## Données (`offers/`, `output/`)

- **`offers/`** : Déposez ici les descriptions de poste (.txt).
- **`output/`** : Les CV générés (.pdf) atterrissent ici.
