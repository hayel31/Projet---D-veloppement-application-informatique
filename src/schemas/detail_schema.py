from pydantic import BaseModel
from typing import Optional

class DetailSchema(BaseModel):
    id: int
    codcde: int  # Référence à la commande
    qte: Optional[int] = 1
    colis: Optional[int] = 1
    commentaire: Optional[str] = None

    class Config:
        orm_mode = True

class DetailCreateSchema(BaseModel):
    codcde: int  # Le code de commande doit être fourni
    qte: Optional[int] = 1
    colis: Optional[int] = 1
    commentaire: Optional[str] = None

    class Config:
        orm_mode = True
