from pydantic import BaseModel

class CommandeCreate(BaseModel):
    codcli: int
    datcde: str
    nbcolis: int = 1
    cdeComt: str = None