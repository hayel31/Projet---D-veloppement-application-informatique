from fastapi import FastAPI
from src.routes import clients, commandes, objets, details  # Utiliser des imports absolus
from src.database import engine, Base  # Importer engine et Base de database.py

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
