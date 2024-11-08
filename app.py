# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from database import get_db, Base, engine
# from models import Client  # Importer les modèles nécessaires
# from pydantic import BaseModel

# # Initialiser FastAPI
# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Bienvenue sur l'API DigiCheese!"}

# # Créer les tables dans la base de données
# Base.metadata.create_all(bind=engine)

# # Modèle Pydantic pour valider les données
# class ClientCreate(BaseModel):
#     genrecli: str
#     nomcli: str
#     prenomcli: str
#     adresse1cli: str = None
#     adresse2cli: str = None
#     adresse3cli: str = None
#     villecli_id: int = None
#     telcli: str = None
#     emailcli: str = None
#     portcli: str = None
#     newsletter: int = 0

# # Endpoint pour récupérer tous les clients
# @app.get("/clients")
# def get_clients(db: Session = Depends(get_db)):
#     clients = db.query(Client).all()
#     return [{"codcli": c.codcli, "nomcli": c.nomcli, "prenomcli": c.prenomcli} for c in clients]

# # Endpoint pour ajouter un client
# @app.post("/clients", response_model=dict)
# def add_client(client: ClientCreate, db: Session = Depends(get_db)):
#     new_client = Client(
#         genrecli=client.genrecli,
#         nomcli=client.nomcli,
#         prenomcli=client.prenomcli,
#         adresse1cli=client.adresse1cli,
#         adresse2cli=client.adresse2cli,
#         adresse3cli=client.adresse3cli,
#         villecli_id=client.villecli_id,
#         telcli=client.telcli,
#         emailcli=client.emailcli,
#         portcli=client.portcli,
#         newsletter=client.newsletter
#     )
#     db.add(new_client)
#     db.commit()
#     db.refresh(new_client)
#     return {"message": "Client ajouté avec succès", "client_id": new_client.codcli}
