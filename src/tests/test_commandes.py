# from fastapi.testclient import TestClient
# from src.main import app  # Assure-toi que le chemin d'importation est correct
# from .setup_test_db import override_get_db, client  # Utilise le même setup que pour les tests de clients

# def test_get_commandes():
#     response = client.get("/commandes")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)

# def test_create_commande():
#     response = client.post("/commandes", json={
#         "codcli": 1,
#         "datcde": "2021-09-01",
#         "nbcolis": 2,
#         "cdeComt": "First order"
#     })
#     assert response.status_code == 200
#     assert response.json()['datcde'] == "2021-09-01"

# def test_get_commande_by_id():
#     # Ajoute une commande pour tester
#     add_response = client.post("/commandes", json={
#         "codcli": 1,
#         "datcde": "2021-10-01",
#         "nbcolis": 1,
#         "cdeComt": "Test get by id"
#     })
#     commande_id = add_response.json()['commande_id']
#     response = client.get(f"/commandes/{commande_id}")
#     assert response.status_code == 200
#     assert response.json()['datcde'] == "2021-10-01"

# def test_update_commande():
#     # Ajoute une commande pour tester la mise à jour
#     add_response = client.post("/commandes", json={
#         "codcli": 1,
#         "datcde": "2021-09-01",
#         "nbcolis": 2,
#         "cdeComt": "Update test"
#     })
#     commande_id = add_response.json()['commande_id']
#     update_response = client.put(f"/commandes/{commande_id}", json={
#         "codcli": 1,
#         "datcde": "2021-09-02",
#         "nbcolis": 3,
#         "cdeComt": "Updated"
#     })
#     assert update_response.status_code == 200
#     assert update_response.json()['datcde'] == "2021-09-02"
#     assert update_response.json()['nbcolis'] == 3

# def test_delete_commande():
#     # Ajoute une commande pour tester la suppression
#     add_response = client.post("/commandes", json={
#         "codcli": 1,
#         "datcde": "2021-09-01",
#         "nbcolis": 2,
#         "cdeComt": "Delete test"
#     })
#     commande_id = add_response.json()['commande_id']
#     delete_response = client.delete(f"/commandes/{commande_id}")
#     assert delete_response.status_code == 200
#     assert delete_response.json() == {"message": "Commande supprimée avec succès"}