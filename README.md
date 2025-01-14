# LinkedIn Job Trend Analysis 📊

## Description
Ce projet est une analyse approfondie des tendances des offres d'emploi sur LinkedIn, réalisée dans le cadre d'un projet de **Data Engineering**. 
Il s'appuie sur des données enrichies et transformées grâce à SQL et Python. 
L'objectif est d'explorer, structurer et extraire des insights pertinents pour mieux comprendre les tendances du marché du travail.

## Objectifs
- **Analyser les données LinkedIn** : Identifier les tendances clés dans les offres d'emploi.
- **Utilisation de SQL** : Transformer, enrichir et organiser les données pour faciliter leur exploration.
- **Visualisation avec Python** : Créer des graphiques clairs et pertinents pour communiquer les résultats.

## Structure du projet
- **Données sources** : Les données utilisées proviennent d'un jeu de données LinkedIn disponible sur Kaggle.
- **SQL** : Utilisé pour transformer et enrichir les données brutes en un format structuré.
- **Python** : Employé pour analyser les données enrichies et générer des visualisations.

## Prérequis
Pour exécuter ce projet, vous aurez besoin de :
- Python 3.8 ou plus récent
- SQL (exécutable dans un environnement tel que MySQL ou PostgreSQL)
- Les bibliothèques Python suivantes :
  ```bash
  pip install pandas numpy matplotlib seaborn
  ```

## Installation et Exécution
1. Clonez ce dépôt sur votre machine :
   ```bash
   git clone https://github.com/alexcanc/linkedin_job_trend_analysis.git
   cd linkedin_job_trend_analysis
   ```
2. Téléchargez les données depuis Kaggle et placez-les dans le répertoire `data`.
3. Exécutez le script SQL pour préparer les données :
   ```sql
   -- Chargez et exécutez le fichier `gold_dataset.sql` dans votre environnement SQL.
   ```
4. Lancez le script principal Python pour analyser les données :
   ```bash
   python main.py
   ```

## Contribution
Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, corriger des bugs ou ajouter des fonctionnalités, n'hésitez pas à soumettre une pull request.

## Auteur
- **Alexandre Canacaris** ([@alexcanc](https://github.com/alexcanc))

---

### Remerciements
Merci à Kaggle pour les données utilisées dans ce projet et à tous ceux qui soutiennent l'open source !
