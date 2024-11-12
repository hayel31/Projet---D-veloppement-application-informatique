from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Client
from pydantic import BaseModel

router = APIRouter()

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

@router.get("/clients")
def get_clients(db: Session = Depends(get_db)):
    clients = db.query(Client).all()
    return clients

@router.post("/clients")
def add_client(client: ClientCreate, db: Session = Depends(get_db)):
    new_client = Client(
        genrecli=client.genrecli,
        nomcli=client.nomcli,
        prenomcli=client.prenomcli,
        adresse1cli=client.adresse1cli,
        adresse2cli=client.adresse2cli,
        adresse3cli=client.adresse3cli,
        villecli_id=client.villecli_id,
        telcli=client.telcli,
        emailcli=client.emailcli,
        portcli=client.portcli,
        newsletter=client.newsletter
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

@router.get("/clients/{client_id}")
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.codcli == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/clients/{client_id}")
def update_client(client_id: int, client: ClientCreate, db: Session = Depends(get_db)):
    existing_client = db.query(Client).filter(Client.codcli == client_id).first()
    if not existing_client:
        raise HTTPException(status_code=404, detail="Client not found")
    for key, value in client.dict().items():
        setattr(existing_client, key, value)
    db.commit()
    db.refresh(existing_client)
    return existing_client

@router.delete("/clients/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.codcli == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    db.delete(client)
    db.commit()
    return {"message": "Client supprimé avec succès"}
