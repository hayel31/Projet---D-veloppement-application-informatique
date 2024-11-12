# src/controllers/client_controller.py
from sqlalchemy.orm import Session
from src.models import Client
from fastapi import HTTPException
from pydantic import BaseModel

class ClientCreate(BaseModel):
    genrecli: str
    nomcli: str
    prenomcli: str
    adresse1cli: str = None
    adresse2cli: str = None
    adresse3cli: str = None
    villecli_id: int = None
    telcli: str = None
    emailcli: str = None
    portcli: str = None
    newsletter: int = 0

def get_all_clients(db: Session):
    return db.query(Client).all()

def create_client(db: Session, client_data: ClientCreate):
    # Vérification de l'unicité de l'email
    if db.query(Client).filter(Client.emailcli == client_data.emailcli).first():
        raise HTTPException(status_code=400, detail="Email already in use")
    
    # Création du client
    new_client = Client(**client_data.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

def get_client_by_id(db: Session, client_id: int):
    client = db.query(Client).filter(Client.codcli == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

def update_client(db: Session, client_id: int, client_data: ClientCreate):
    client = db.query(Client).filter(Client.codcli == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    # Vérification de l'unicité de l'email si l'email est modifié
    if client_data.emailcli and client_data.emailcli != client.emailcli:
        if db.query(Client).filter(Client.emailcli == client_data.emailcli).first():
            raise HTTPException(status_code=400, detail="Email already in use")

    # Mise à jour des champs du client
    for key, value in client_data.dict(exclude_unset=True).items():
        setattr(client, key, value)
    db.commit()
    db.refresh(client)
    return client

def delete_client(db: Session, client_id: int):
    client = db.query(Client).filter(Client.codcli == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    db.delete(client)
    db.commit()
    return {"message": "Client supprimé avec succès"}
