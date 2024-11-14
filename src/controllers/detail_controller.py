from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models import Detail
from src.schemas.detail_schema import DetailSchema, DetailCreateSchema

def get_all_details(db: Session):
    """Récupère tous les détails."""
    return db.query(Detail).all()

def create_detail(db: Session, detail_data: DetailCreateSchema):
    """Crée un nouveau détail dans la base de données."""
    new_detail = Detail(**detail_data.dict())
    db.add(new_detail)
    db.commit()
    db.refresh(new_detail)
    return new_detail

def get_detail_by_id(db: Session, detail_id: int):
    """Récupère un détail par son ID."""
    detail = db.query(Detail).filter(Detail.id == detail_id).first()
    if not detail:
        raise HTTPException(status_code=404, detail="Détail non trouvé")
    return detail

def update_detail(db: Session, detail_id: int, detail_data: DetailCreateSchema):
    """Met à jour un détail par son ID."""
    detail = db.query(Detail).filter(Detail.id == detail_id).first()
    if not detail:
        raise HTTPException(status_code=404, detail="Détail non trouvé")
    
    # Met à jour les champs qui sont dans la requête
    for key, value in detail_data.dict(exclude_unset=True).items():
        setattr(detail, key, value)
    db.commit()
    db.refresh(detail)
    return detail

def delete_detail(db: Session, detail_id: int):
    """Supprime un détail par son ID."""
    detail = db.query(Detail).filter(Detail.id == detail_id).first()
    if not detail:
        raise HTTPException(status_code=404, detail="Détail non trouvé")
    db.delete(detail)
    db.commit()
    return {"message": "Détail supprimé avec succès"}