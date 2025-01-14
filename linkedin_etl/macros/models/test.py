from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import os

# Assurez-vous que le chemin vers le fichier de clé est correct et accessible
# Utilisez le chemin absolu si le chemin relatif ne fonctionne pas
key_path = os.path.expanduser("~/dbt_keys/linkedin123456-4733c84e9892.json")

# Authentification
credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# Charger les données depuis BigQuery
query = """
    SELECT * FROM `linkedin123456.bronze_silver.cleaned_skills`
"""
df_skills = client.query(query).to_dataframe()

# Fonction pour traiter les données et conserver uniquement la compétence la plus commune
def process_data(df):
    # Séparer les compétences et les compter
    skills_expanded = df['job_skills'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True).to_frame('job_skill')
    df = df.drop('job_skills', axis=1).join(skills_expanded).reset_index(drop=True)

    # Calculer la compétence la plus fréquente pour chaque job_link
    most_common_skills = df.groupby('job_link')['job_skill'].agg(lambda x: x.mode()[0] if not x.mode().empty else None).reset_index()

    return most_common_skills

# Appliquer la transformation
df_most_common_skills = process_data(df_skills)

# Optionnel: Sauvegarder le résultat dans une nouvelle table BigQuery
# Remplacez 'your_dataset.new_table' par le nom de votre dataset et la nouvelle table
table_id = 'linkedin123456.bronze_silver.cleaned_skills_most_common'
job = client.load_table_from_dataframe(df_most_common_skills, table_id)

# Attendre la fin de l'opération de chargement
job.result()

print(f"Les données ont été chargées avec succès dans la table '{table_id}'.")
