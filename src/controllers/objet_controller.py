from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models import Objet
from src.schemas.objet_schema import ObjetSchema, ObjetCreateSchema

def get_all_objets(db: Session):
    """Récupère tous les objets."""
    return db.query(Objet).all()

def create_objet(db: Session, objet_data: ObjetCreateSchema):
    """Crée un nouvel objet avec les données fournies."""
    # Crée un nouvel objet à partir des données reçues
    new_objet = Objet(**objet_data.dict())
    db.add(new_objet)
    db.commit()
    db.refresh(new_objet)
    return new_objet

def get_objet_by_id(db: Session, objet_id: int):
    """Récupère un objet par son ID."""
    objet = db.query(Objet).filter(Objet.codobj == objet_id).first()
    if not objet:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
    return objet

def update_objet(db: Session, objet_id: int, objet_data: ObjetCreateSchema):
    """Met à jour un objet avec les nouvelles données."""
    objet = db.query(Objet).filter(Objet.codobj == objet_id).first()
    if not objet:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
    
    # Met à jour uniquement les champs définis dans la requête
    for key, value in objet_data.dict(exclude_unset=True).items():
        setattr(objet, key, value)
    db.commit()
    db.refresh(objet)
    return objet

def delete_objet(db: Session, objet_id: int):
    """Supprime un objet par son ID."""
    objet = db.query(Objet).filter(Objet.codobj == objet_id).first()
    if not objet:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
    db.delete(objet)
    db.commit()
    return {"message": "Objet supprimé avec succès"}