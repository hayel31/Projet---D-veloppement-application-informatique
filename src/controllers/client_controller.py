# src/controllers/client_controller.py
from sqlalchemy.orm import Session
from models import Client
from fastapi import HTTPException

def get_all_clients(db: Session):
    return db.query(Client).all()

def create_client(db: Session, client_data):
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

def update_client(db: Session, client_id: int, client_data):
    client = db.query(Client).filter(Client.codcli == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    for key, value in client_data.dict().items():
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
