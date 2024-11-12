# src/schemas/client_schema.py
from pydantic import BaseModel

class ClientCreate(BaseModel):
    genrecli: str
    nomcli: str
    prenomcli: str
    adresse1cli: str = None
    adresse2cli: str = None
    adresse3cli: str = None
    villecli_id: int = None
    telcli: str = None
    emailcli: str = None
    portcli: str = None
    newsletter: int = 0

class ClientUpdate(BaseModel):
    genrecli: str
    nomcli: str
    prenomcli: str
    adresse1cli: str = None
    adresse2cli: str = None
    adresse3cli: str = None
    villecli_id: int = None
    telcli: str = None
    emailcli: str = None
    portcli: str = None
    newsletter: int = 0
