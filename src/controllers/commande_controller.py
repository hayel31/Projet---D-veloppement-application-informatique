# src/controllers/commande_controller.py
from sqlalchemy.orm import Session
from src.models import Commande
from fastapi import HTTPException
from pydantic import BaseModel

class CommandeCreate(BaseModel):
    codcli: int
    datcde: str
    nbcolis: int = 1
    cdeComt: str = None

def get_all_commandes(db: Session):
    return db.query(Commande).all()

def create_commande(db: Session, commande_data: CommandeCreate):
    new_commande = Commande(**commande_data.dict())
    db.add(new_commande)
    db.commit()
    db.refresh(new_commande)
    return new_commande

def get_commande_by_id(db: Session, commande_id: int):
    commande = db.query(Commande).filter(Commande.codcde == commande_id).first()
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    return commande

def update_commande(db: Session, commande_id: int, commande_data: CommandeCreate):
    commande = db.query(Commande).filter(Commande.codcde == commande_id).first()
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    for key, value in commande_data.dict().items():
        setattr(commande, key, value)
    db.commit()
    return commande

def delete_commande(db: Session, commande_id: int):
    commande = db.query(Commande).filter(Commande.codcde == commande_id).first()
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    db.delete(commande)
    db.commit()
    return {"message": "Commande supprimée avec succès"}
