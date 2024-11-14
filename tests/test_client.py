import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.main import app
from src.database import SessionLocal
from src.models import Client
from src.schemas.client_schema import ClientCreate, ClientUpdate
import unittest
from fastapi.testclient import TestClient
from sqlalchemy.exc import IntegrityError

class TestClientCRUD(unittest.TestCase):
    def setUp(self):
        # Initialize the test client and database session
        self.client = TestClient(app)
        self.db = SessionLocal()

        # Clean up the database before each test to ensure a fresh start
        self.db.query(Client).delete()
        self.db.commit()

        # Create a test client
        self.test_client_data = {
            "nomcli": "Test Client",
            "emailcli": "test@example.com",
            "genrecli": "M",
        }
        self.test_client = Client(**self.test_client_data)
        self.db.add(self.test_client)
        self.db.commit()
        self.db.refresh(self.test_client)

    def tearDown(self):
        # Clean up the test client and database
        self.db.delete(self.test_client)
        self.db.commit()
        self.db.close()

    def test_route_hello_world(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Bienvenue sur l'API DigiCheese!"})

    def test_get_client_by_id(self):
        response = self.client.get(f"/clients/{self.test_client.codcli}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["nomcli"], "Test Client")
        self.assertEqual(response.json()["emailcli"], "test@example.com")

    # def test_create_client(self):
    #     new_client_data = {
    #         "nomcli": "New Client",
    #         "emailcli": "newclient@example.com",
    #         "genrecli": "F",
    #     }
    #     response = self.client.post("/clients", json=new_client_data)

    #     # Check response status and content
    #     self.assertEqual(response.status_code, 200, msg=f"Expected status code 200, got {response.status_code}. Response body: {response.json()}")

    #     # Verify the client was actually created in the database
    #     created_client = self.db.query(Client).filter(Client.emailcli == "newclient@example.com").first()
    #     self.assertIsNotNone(created_client, "The client should have been created but was not found in the database.")

    def test_update_client(self):
        update_data = {
            "nomcli": "Updated Client",
            "emailcli": "updated@example.com",
            "genrecli": "M",
        }
        response = self.client.put(f"/clients/{self.test_client.codcli}", json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["nomcli"], "Updated Client")
        self.assertEqual(response.json()["emailcli"], "updated@example.com")

    def test_delete_client(self):
        response = self.client.delete(f"/clients/{self.test_client.codcli}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Client deleted successfully"})

        response = self.client.get(f"/clients/{self.test_client.codcli}")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()