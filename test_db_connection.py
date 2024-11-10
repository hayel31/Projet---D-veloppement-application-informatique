import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Spécifiez le chemin complet vers le fichier .env
env_path = r"C:\Users\youss\Desktop\Formation\API1\Projet---D-veloppement-application-informatique\.env"
load_dotenv(env_path)

# Charger les variables d'environnement
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

try:
    # Établir la connexion à la base de données
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )

    if connection.is_connected():
        print("Connexion réussie à la base de données")
        db_info = connection.get_server_info()
        print("Version du serveur MySQL :", db_info)

except Error as e:
    print("Erreur lors de la connexion à la base de données :", e)

finally:
    if connection.is_connected():
        connection.close()
        print("Connexion à la base de données fermée")