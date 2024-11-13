import sys
import os
import unittest
from fastapi.testclient import TestClient

# Ajouter 'src' au chemin d'importation pour que Python puisse trouver main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Maintenant tu peux importer l'application FastAPI depuis main
from main import app

class TestClientRoutes(unittest.TestCase):
    def setUp(self):
        # Récupère un client de test
        self.client = TestClient(app)
    
    def test_get_all_clients_empty(self):
        # Test pour la route GET /clients quand la base de données est vide
        response = self.client.get("/clients")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])  # On attend une liste vide si aucun client n'est créé

    def test_create_client(self):
        # Test de la création d'un client
        response = self.client.post(
            "/clients",
            json={"emailcli": "test@domain.com", "nomcli": "John", "prenomcli": "Doe", "adressecli": "123 Rue", "telephonecli": "1234567890"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("emailcli", response.json())
        self.assertEqual(response.json()["emailcli"], "test@domain.com")
        
    def test_get_all_clients_with_data(self):
        # Ajout d'un client pour tester la récupération
        self.client.post(
            "/clients",
            json={"emailcli": "test2@domain.com", "nomcli": "Alice", "prenomcli": "Wonder", "adressecli": "789 Avenue", "telephonecli": "9876543210"}
        )
        
        # Test de la route GET /clients après ajout d'un client
        response = self.client.get("/clients")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)  # On s'attend à un seul client dans la réponse
        self.assertEqual(response.json()[0]["emailcli"], "test2@domain.com")

if __name__ == "__main__":
    unittest.main()
