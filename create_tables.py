from src.models import * 
from src.database import engine, Base

Base.metadata.create_all(bind=engine)  # Créer les tables dans la base de données
print("Tables créées avec succès.")