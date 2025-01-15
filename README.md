Health Calculator Service
=========================

Health Calculator Service est une API Flask qui permet de réaliser des calculs de santé comme l'IMC (BMI) et la dépense énergétique totale(BMR).

**Fonctionnalités principales :**

*   Calcul de l'IMC (Body Mass Index).
    
*   Calcul de la dépense énergétique quotidienne (BMR).
    

**Structure du projet :**

Health-calculator-service/
├── app.py
├── health_utils.py
├── test.py
├── requirements.txt
├── Makefile
├── Dockerfile
├── .gitignore
├──.templates/
│   └── index.html
├── .github/
│   └── workflows/
│       └── main_python-app-elyess.yml

*   app.py : Fichier principal de l'application Flask.
    
*   health_utils.py : Fonctions utilitaires pour les calculs de santé.
    
*   test.py : Tests unitaires pour vérifier le bon fonctionnement.
    
*   requirements.txt : Liste des dépendances Python.
    
*   Dockerfile : Fichier pour créer une image Docker de l'application.
    
*   Makefile : Automatisation des tâches courantes (tests, installation).
    
*   templates/home.html : Template HTML pour l'interface utilisateur.
    
*   .github/workflows/ci.yml : Workflow GitHub Actions pour CI/CD.
    

**Prérequis :**

*   Python 3.x
    
*   Flask
    
*   Docker (optionnel pour exécuter via un conteneur)
    

**Installation :**

1.  Cloner le dépôt :git clone https://github.com/elyessrj/health-calculator-service.git
    
2.  Aller dans le dossier :cd health-calculator-service
    
3.  Créer un environnement virtuel et l'activer :Sous Linux/Mac :python -m venv venv && source venv/bin/activateSous Windows :python -m venv venv && venv\\Scripts\\activate
    
4.  Installer les dépendances :pip install -r requirements.txt
    

**Utilisation :**

1.  Lancer le serveur Flask :python app.py
    
2.  Accéder à l'application dans un navigateur à l'adresse :http://127.0.0.1:5005/
    
3.  Ou bien Accéder à l'application deployer avec Azure dans un navigateur à l'adresse :https://python-app-elyess-gxd8b3gabnh6dne3.francecentral-01.azurewebsites.net/

**Tests unitaires :**Pour exécuter les tests unitaires :python test.py

**Exécution avec Docker :**

1.  Construire l'image Docker :docker build -t health-calculator-service .
    
2.  Lancer le conteneur :docker run -p 5005:5005 health-calculator-service
    

**Intégration Continue :**Ce projet utilise GitHub Actions pour l'intégration continue.Le workflow est défini dans .github/workflows/ci.yml et se déclenche automatiquement lors des push.