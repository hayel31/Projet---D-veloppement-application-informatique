from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.controllers.detail_controller import (
    get_all_details,
    create_detail,
    get_detail_by_id,
    update_detail,
    delete_detail
)
from src.schemas.detail_schema import DetailSchema, DetailCreateSchema
from src.database import get_db

router = APIRouter()

@router.get("/details", response_model=list[DetailSchema], tags=["Détails"])
def read_all_details(db: Session = Depends(get_db)):
    """Récupère tous les détails."""
    return get_all_details(db)

@router.post("/details", response_model=DetailSchema, tags=["Détails"])
def create_new_detail(detail_data: DetailCreateSchema, db: Session = Depends(get_db)):
    """Crée un nouveau détail."""
    return create_detail(db, detail_data)

@router.get("/details/{detail_id}", response_model=DetailSchema, tags=["Détails"])
def read_detail(detail_id: int, db: Session = Depends(get_db)):
    """Récupère un détail par son ID."""
    detail = get_detail_by_id(db, detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Détail non trouvé")
    return detail

@router.put("/details/{detail_id}", response_model=DetailSchema, tags=["Détails"])
def update_existing_detail(detail_id: int, detail_data: DetailCreateSchema, db: Session = Depends(get_db)):
    """Met à jour un détail par son ID."""
    detail = update_detail(db, detail_id, detail_data)
    if not detail:
        raise HTTPException(status_code=404, detail="Détail non trouvé")
    return detail

@router.delete("/details/{detail_id}", tags=["Détails"])
def delete_existing_detail(detail_id: int, db: Session = Depends(get_db)):
    """Supprime un détail par son ID."""
    result = delete_detail(db, detail_id)
    if not result:
        raise HTTPException(status_code=404, detail="Détail non trouvé")
    return result
