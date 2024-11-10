from fastapi import FastAPI
from .routes import clients, commandes  # Utiliser des imports relatifs
from database import engine, Base  # Importez engine et Base de database.py

# Initialiser l'application FastAPI
app = FastAPI()

# Créer les tables dans la base de données si elles n'existent pas encore
Base.metadata.create_all(bind=engine)

# Inclure les routeurs secondaires
app.include_router(clients.router)
app.include_router(commandes.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API DigiCheese!"}
