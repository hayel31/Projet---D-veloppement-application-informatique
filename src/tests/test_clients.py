# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from src.main import app  # Assure-toi que le chemin d'importation est correct
# from src.database import Base, get_db

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Utilise une base de données de test

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base.metadata.create_all(bind=engine)

# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# app.dependency_overrides[get_db] = override_get_db

# client = TestClient(app)

# def test_get_clients():
#     response = client.get("/clients")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)

# def test_create_client():
#     response = client.post("/clients", json={
#         "genrecli": "M",
#         "nomcli": "Doe",
#         "prenomcli": "John",
#         "emailcli": "john.doe@example.com"
#     })
#     assert response.status_code == 200
#     data = response.json()
#     assert data['nomcli'] == 'Doe'

# def test_delete_client():
#     # Ajoute un client
#     response = client.post("/clients", json={"nomcli": "Doe", "prenomcli": "John", "emailcli": "delete@example.com"})
#     client_id = response.json()['id']
#     # Supprime le client
#     response = client.delete(f"/clients/{client_id}")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Client deleted successfully"}