from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.controllers.client_controller import create_client, get_all_clients, get_client_by_id, update_client, delete_client
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

@router.get("/clients", response_model=list[ClientCreate], summary="Retrieve all clients", description="Returns a list of all clients in the database.")
def get_clients(db: Session = Depends(get_db)):
    return get_all_clients(db)

@router.post("/clients", response_model=ClientCreate, summary="Create a new client", description="Creates a new client in the database and returns the created client object.")
def add_client(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db, client)

@router.get("/clients/{client_id}", response_model=ClientCreate, summary="Retrieve a client by ID", description="Returns a single client identified by its ID.")
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = get_client_by_id(db, client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/clients/{client_id}", response_model=ClientCreate, summary="Update a client", description="Updates an existing client identified by its ID and returns the updated client object.")
def update_client_details(client_id: int, client: ClientCreate, db: Session = Depends(get_db)):
    return update_client(db, client_id, client)

@router.delete("/clients/{client_id}", summary="Delete a client", description="Deletes a client identified by its ID and returns a success message.")
def remove_client(client_id: int, db: Session = Depends(get_db)):
    result = delete_client(db, client_id)
    if not result:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"message": "Client deleted successfully"}
