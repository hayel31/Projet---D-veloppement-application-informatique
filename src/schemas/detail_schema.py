from pydantic import BaseModel
from typing import Optional

class DetailSchema(BaseModel):
    id: int | None = None
    codcde: int | None = None 
    qte: int | None = None
    colis: int | None = None
    commentaire:  str | None = None


class DetailCreateSchema(BaseModel):
    codcde: int | None = None 
    qte: int | None = None
    colis: int | None = None
    commentaire:  str | None = None