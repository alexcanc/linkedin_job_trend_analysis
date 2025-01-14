from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import os

# Assurez-vous que le chemin vers le fichier de clé est correct et accessible
key_path = os.path.expanduser("~/dbt_keys/linkedin123456-4733c84e9892.json")

# Authentification
credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# Charger les données depuis BigQuery
query = """
    SELECT * FROM `linkedin123456.bronze_silver.cleaned_skills`
"""
df_skills = client.query(query).to_dataframe()

# Fonction pour traiter les données et sélectionner la première compétence de la liste pour chaque job
def process_data(df):
    # Sélectionner directement la première compétence de la liste pour chaque job_link
    df['first_skill'] = df['job_skills'].apply(lambda x: x.split(', ')[0] if x else None)

    # Garder uniquement les colonnes 'job_link' et 'first_skill'
    first_skills = df[['job_link', 'first_skill']].drop_duplicates()

    return first_skills

# Appliquer la transformation
df_first_skill = process_data(df_skills)

# Afficher les premières lignes du DataFrame résultant pour vérification
print(df_first_skill.head())

# Optionnel: Sauvegarder le résultat dans une nouvelle table BigQuery
# Remplacez 'your_dataset.new_table' par le nom de votre dataset et la nouvelle table
table_id = 'linkedin123456.bronze_silver.cleaned_skills_first_skill'
job = client.load_table_from_dataframe(df_first_skill, table_id)

# Attendre la fin de l'opération de chargement
job.result()

print(f"Les données ont été chargées avec succès dans la table '{table_id}'.")
