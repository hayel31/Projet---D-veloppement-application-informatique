from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.controllers.objet_controller import (
    get_all_objets,
    create_objet,
    get_objet_by_id,
    update_objet,
    delete_objet
)
from src.schemas.objet_schema import ObjetSchema, ObjetCreateSchema
from src.database import get_db

router = APIRouter()

@router.get("/objets", response_model=list[ObjetSchema], tags=["Objets"])
def read_all_objets(db: Session = Depends(get_db)):
    """Récupère tous les objets."""
    return get_all_objets(db)

@router.post("/objets", response_model=ObjetSchema, tags=["Objets"])
def create_new_objet(objet_data: ObjetCreateSchema, db: Session = Depends(get_db)):
    """Crée un nouvel objet."""
    return create_objet(db, objet_data)

@router.get("/objets/{objet_id}", response_model=ObjetSchema, tags=["Objets"])
def read_objet(objet_id: int, db: Session = Depends(get_db)):
    """Récupère un objet par son ID."""
    objet = get_objet_by_id(db, objet_id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
    return objet

@router.put("/objets/{objet_id}", response_model=ObjetSchema, tags=["Objets"])
def update_existing_objet(objet_id: int, objet_data: ObjetCreateSchema, db: Session = Depends(get_db)):
    """Met à jour un objet par son ID."""
    objet = update_objet(db, objet_id, objet_data)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
    return objet

@router.delete("/objets/{objet_id}", tags=["Objets"])
def delete_existing_objet(objet_id: int, db: Session = Depends(get_db)):
    """Supprime un objet par son ID."""
    result = delete_objet(db, objet_id)
    if not result:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
    return result
