
# Projet DigiCheese - API Backend

Ce projet est une API backend pour la gestion des données de la fromagerie DigiCheese, développée avec FastAPI et SQLAlchemy pour interagir avec une base de données MySQL.

## Prérequis

Assurez-vous que les éléments suivants sont installés sur votre machine :
- **Python 3.8+**
- **MySQL** (ou MariaDB)
- **Git**

## Installation et Configuration

### 1. Cloner le dépôt

Commencez par cloner le dépôt Git en local et placez-vous dans le dossier du projet :

```bash
git clone <URL_DU_DEPOT>
cd <nom_du_dossier_du_projet>
```

### 2. Créer un Environnement Virtuel

Créez un environnement virtuel Python pour installer les dépendances :

```bash
python -m venv .venv
```

Activez l’environnement virtuel :
- **Sur Windows** : `.\.venv\Script\activate`
- **Sur macOS/Linux** : `source .venv/bin/activate`

### 3. Installer les Dépendances

Installez toutes les dépendances nécessaires avec la commande suivante :

```bash
pip install -r requirements.txt
```

### 4. Configurer les Variables d’Environnement

Créez un fichier `.env` à la racine du projet pour stocker les informations de connexion à la base de données. Utilisez le modèle ci-dessous :

```plaintext
DB_USER=<votre_utilisateur_mysql>
DB_PASSWORD=<votre_mot_de_passe_mysql>
DB_HOST=localhost
DB_PORT=3306
DB_NAME=digicheese_db
```

Remplacez `<votre_utilisateur_mysql>` et `<votre_mot_de_passe_mysql>` par vos propres informations.

### 5. Créer la Base de Données

1. Ouvrez MySQL (ou MariaDB) et créez la base de données si elle n’existe pas encore :

   ```sql
   CREATE DATABASE digicheese_db;
   ```

2. Assurez-vous que les informations dans le fichier `.env` correspondent à votre configuration.

### 6. Exécuter le Script de Création des Tables

Exécutez le script de base de données pour créer toutes les tables nécessaires dans `digicheese_db` :

```bash
python src/database.py
```

Vous devriez voir le message "Tables créées avec succès."

### 7. Structure du Projet

Votre projet devrait avoir l’architecture de dossier suivante :
```
projet_digicheese/
├── src/
│   ├── main.py              # Point d'entrée principal de l'application FastAPI
│   ├── database.py          # Configuration de la base de données
│   ├── models.py            # Modèles SQLAlchemy pour les tables
│   ├── routes/              # Dossier pour les fichiers de routes
│   │   ├── __init__.py      # Fichier pour marquer le dossier routes comme un package Python
│   │   ├── clients.py       # Fichier de route pour gérer les clients
│   │   └── commandes.py     # Fichier de route pour gérer les commandes
├── .env                     # Variables d'environnement pour la base de données
├── requirements.txt         # Liste des dépendances Python
└── README.md                # Documentation du projet
```

### 8. Lancer le Serveur

Démarrez le serveur FastAPI avec Uvicorn :

```bash
uvicorn src.main:app --reload
```

Le serveur devrait maintenant tourner sur [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Étapes de Test des Modifications

Avant de créer des tests automatisés, vous pouvez tester les modifications manuellement en utilisant Swagger ou Postman.

### 1. Démarrer le Serveur FastAPI

Lancez le serveur avec Uvicorn pour tester l'API localement.

```bash
uvicorn src.main:app --reload
```

Le serveur sera accessible à l’adresse `http://127.0.0.1:8000`.

### 2. Tester les Endpoints avec Swagger

FastAPI fournit une documentation interactive pour faciliter les tests.

1. Ouvrez un navigateur et allez à [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
2. Vous verrez tous les endpoints de l'API avec des options pour les tester.
3. Cliquez sur chaque endpoint et utilisez l'option "Try it out" pour tester :
   - **GET /clients** : Récupère la liste des clients pour vérifier que la lecture fonctionne.
   - **POST /clients** : Ajoute un client en renseignant les champs requis et en cliquant sur "Execute".
   - **PUT /clients/{client_id}** : Met à jour un client existant en indiquant un `client_id` valide.
   - **DELETE /clients/{client_id}** : Supprime un client existant avec un `client_id` valide. Utilisez un `client_id` inexistant pour vérifier que l'erreur 404 est renvoyée.

### 3. Vérifier les Résultats

Vérifiez que les actions de création, mise à jour, et suppression fonctionnent comme prévu. Assurez-vous que :
- Les clients sont correctement ajoutés, mis à jour ou supprimés.
- Les erreurs 404 sont renvoyées lorsque vous tentez d'accéder à un client inexistant.

Une fois ces étapes manuelles validées, vous pouvez passer à la création de tests automatisés pour garantir la qualité continue du code.

