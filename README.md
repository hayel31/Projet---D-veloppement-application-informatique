
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
- **Sur Windows** : `.\.venv\Scriptsctivate`
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
python database.py
```

Vous devriez voir le message "Tables créées avec succès."

### 7. Lancer le Serveur

Démarrez le serveur FastAPI avec Uvicorn :

```bash
uvicorn app:app --reload
```

Le serveur devrait maintenant tourner sur [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 8. Tester l’API

Vous pouvez accéder à la documentation interactive de l'API avec Swagger à l'adresse suivante : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

## Structure du Projet

- **app.py** : Fichier principal contenant les endpoints de l'API.
- **database.py** : Fichier de configuration de la base de données.
- **models.py** : Définitions des modèles SQLAlchemy pour les tables.
- **.env** : Variables d'environnement pour la configuration de la base de données (ne pas oublier de le créer).
- **requirements.txt** : Liste des dépendances Python.

## Conventions de Développement

- Utilisez des branches individuelles pour chaque développeur (`git checkout -b <nom_de_branche>`) et effectuez un `pull request` pour la revue du code avant fusion dans la branche principale.
- Mettez à jour régulièrement les dépendances dans `requirements.txt` si de nouvelles bibliothèques sont ajoutées.
