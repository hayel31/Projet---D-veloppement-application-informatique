from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.controllers.commande_controller import (
    get_all_commandes, create_commande, get_commande_by_id,
    update_commande, delete_commande
)
from src.schemas.commande_schema import CommandeCreate

router = APIRouter()

@router.get("/commandes", tags=["Commandes"], summary="Retrieve all commandes", description="Returns a list of all commandes in the database.")
def get_commandes(db: Session = Depends(get_db)):
    return get_all_commandes(db)

@router.post("/commandes", tags=["Commandes"], summary="Create a new commande", description="Creates a new commande in the database and returns the created commande object.")
def add_commande(commande: CommandeCreate, db: Session = Depends(get_db)):
    return create_commande(db, commande)

@router.get("/commandes/{commande_id}", tags=["Commandes"], summary="Retrieve a commande by ID", description="Returns a single commande identified by its ID.")
def get_commande(commande_id: int, db: Session = Depends(get_db)):
    return get_commande_by_id(db, commande_id)

@router.put("/commandes/{commande_id}", tags=["Commandes"], summary="Update a commande", description="Updates an existing commande identified by its ID and returns the updated commande object.")
def update_commande_details(commande_id: int, commande: CommandeCreate, db: Session = Depends(get_db)):
    return update_commande(db, commande_id, commande)

@router.delete("/commandes/{commande_id}", tags=["Commandes"], summary="Delete a commande", description="Deletes a commande identified by its ID and returns a success message.")
def remove_commande(commande_id: int, db: Session = Depends(get_db)):
    return delete_commande(db, commande_id)