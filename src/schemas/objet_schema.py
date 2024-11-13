from pydantic import BaseModel
from typing import Optional

class ObjetSchema(BaseModel):
    codobj: int
    libobj: Optional[str] = None
    tailleobj: Optional[str] = None
    puobj: Optional[float] = 0.0000
    poidsobj: Optional[float] = 0.0000
    indispobj: Optional[int] = 0
    o_imp: Optional[int] = 0
    o_aff: Optional[int] = 0
    o_cartp: Optional[int] = 0
    points: Optional[int] = 0
    o_ordre_aff: Optional[int] = 0

    class Config:
        orm_mode = True

class ObjetCreateSchema(BaseModel):
    libobj: Optional[str] = None
    tailleobj: Optional[str] = None
    puobj: Optional[float] = 0.0000
    poidsobj: Optional[float] = 0.0000
    indispobj: Optional[int] = 0
    o_imp: Optional[int] = 0
    o_aff: Optional[int] = 0
    o_cartp: Optional[int] = 0
    points: Optional[int] = 0
    o_ordre_aff: Optional[int] = 0

    class Config:
        orm_mode = True
