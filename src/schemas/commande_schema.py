from pydantic import BaseModel
from datetime import date

class CommandeCreate(BaseModel):
    codcli:  int | None = None
    datcde:  date | None = None
    nbcolis: int | None = None
    cdeComt: str | None = None
    cheqcli: int | None = None