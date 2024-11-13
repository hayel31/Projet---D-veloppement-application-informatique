from sqlalchemy.orm import Session
from src.models import Client
from fastapi import HTTPException
from src.schemas.client_schema import ClientCreate, ClientUpdate

def get_all_clients(db: Session):
    return db.query(Client).all()

def create_client(db: Session, client_data: ClientCreate):
    if db.query(Client).filter(Client.emailcli == client_data.emailcli).first():
        raise HTTPException(status_code=400, detail="Email already in use")
    
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

def get_client_by_name(db: Session, client_name: str):
    client = db.query(Client).filter(Client.nomcli == client_name).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

def update_client(db: Session, client_id: int, client_data: ClientUpdate):
    client = db.query(Client).filter(Client.codcli == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    if client_data.emailcli and client_data.emailcli != client.emailcli:
        if db.query(Client).filter(Client.emailcli == client_data.emailcli).first():
            raise HTTPException(status_code=400, detail="Email already in use")

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
