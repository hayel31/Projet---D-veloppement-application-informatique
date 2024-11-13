from fastapi import FastAPI
from .routes import clients, commandes, objets, details  # Utiliser des imports relatifs
from src.database import engine, Base  # Importez engine et Base de database.py
from src.models import Client, Commande,  Objet, Detail
# Initialiser l'application FastAPI
app = FastAPI()

# Créer les tables dans la base de données si elles n'existent pas encore
Base.metadata.create_all(bind=engine)

# Inclure les routeurs secondaires
app.include_router(clients.router)
app.include_router(commandes.router)
app.include_router(objets.router)
app.include_router(details.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API DigiCheese!"}
