# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-09

### Ajouté
- Initialisation du projet de génération de CV.
- `scripts/adapt_cv.py` : Script principal pour l'orchestration (analyse, modification, compilation).
- `awesome-source-cv.cls` : Classe LaTeX personnalisée avec marges réduites (0.8cm) pour optimiser l'espace.
- `sections/` : Modularisation du contenu LaTeX (expériences, compétences, etc.).
- Support de l'injection dynamique de mots-clés via API LLM.

### Modifié
- Ajustement des espacements de titres dans la classe LaTeX pour gagner de la place verticale.
- Configuration du `.gitignore` pour exclure les artefacts LaTeX et Python.
