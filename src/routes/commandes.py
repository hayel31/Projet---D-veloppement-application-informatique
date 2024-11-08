from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Commande
from pydantic import BaseModel

router = APIRouter()

class CommandeCreate(BaseModel):
    codcli: int
    datcde: str
    nbcolis: int = 1
    cdeComt: str = None

@router.get("/commandes")
def get_commandes(db: Session = Depends(get_db)):
    commandes = db.query(Commande).all()
    return [{"codcde": c.codcde, "codcli": c.codcli, "datcde": c.datcde} for c in commandes]

@router.post("/commandes")
def add_commande(commande: CommandeCreate, db: Session = Depends(get_db)):
    new_commande = Commande(
        codcli=commande.codcli,
        datcde=commande.datcde,
        nbcolis=commande.nbcolis,
        cdeComt=commande.cdeComt
    )
    db.add(new_commande)
    db.commit()
    db.refresh(new_commande)
    return {"message": "Commande ajoutée avec succès", "commande_id": new_commande.codcde}
