# src/routes/clients.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from pydantic import BaseModel
from controllers import client_controller

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
    return client_controller.get_all_clients(db)

@router.post("/clients")
def add_client(client: ClientCreate, db: Session = Depends(get_db)):
    return client_controller.create_client(db, client)

@router.get("/clients/{client_id}")
def get_client(client_id: int, db: Session = Depends(get_db)):
    return client_controller.get_client_by_id(db, client_id)

@router.put("/clients/{client_id}")
def update_client(client_id: int, client: ClientCreate, db: Session = Depends(get_db)):
    return client_controller.update_client(db, client_id, client)

@router.delete("/clients/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    return client_controller.delete_client(db, client_id)
