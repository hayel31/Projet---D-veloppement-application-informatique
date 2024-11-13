from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
env_path = r"C:\Users\youss\Desktop\Formation\API1\Projet---D-veloppement-application-informatique\.env"
load_dotenv(env_path)

# URL de connexion de la base en utilisant les variables d'environnement
SQLALCHEMY_DATABASE_URL = (
    f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

# Configuration de l'engine pour SQLAlchemy avec la base de données
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"collation": "utf8mb4_general_ci"})

# Déclaration de la base pour créer des modèles et faire le mapping
Base = declarative_base()

# Création de la session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Fonction pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()