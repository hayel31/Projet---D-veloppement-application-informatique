from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.controllers.commande_controller import (
    get_all_commandes, create_commande, get_commande_by_id,
    update_commande, delete_commande
)
from src.schemas.commande_schema import CommandeCreate

router = APIRouter()

@router.get("/commandes", tags=["Commandes"])
def get_commandes(db: Session = Depends(get_db)):
    """Récupère toutes les commandes."""
    return get_all_commandes(db)

@router.post("/commandes", tags=["Commandes"])
def add_commande(commande: CommandeCreate, db: Session = Depends(get_db)):
    """Crée une nouvelle commande."""
    return create_commande(db, commande)

@router.get("/commandes/{commande_id}", tags=["Commandes"])
def get_commande(commande_id: int, db: Session = Depends(get_db)):
    """Récupère une commande par son ID."""
    return get_commande_by_id(db, commande_id)

@router.put("/commandes/{commande_id}", tags=["Commandes"])
def update_commande_details(commande_id: int, commande: CommandeCreate, db: Session = Depends(get_db)):
    """Met à jour une commande par son ID."""
    return update_commande(db, commande_id, commande)

@router.delete("/commandes/{commande_id}", tags=["Commandes"])
def remove_commande(commande_id: int, db: Session = Depends(get_db)):
    """Supprime une commande par son ID."""
    return delete_commande(db, commande_id)
