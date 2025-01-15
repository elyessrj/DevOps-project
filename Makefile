# Définition des cibles "phony", c'est-à-dire des cibles qui ne correspondent pas à un fichier
.PHONY: help init install build run-docker run-app test test-api

# Commande "help" : affiche les instructions des commandes disponibles dans le Makefile
help:
	@echo "Makefile commands:"
	@echo "  init       Setup and Activate the virtual environment"  # Description de la commande "init"
	@echo "  install    Install project dependencies"               # Description de la commande "install"
	@echo "  build      Build the Docker image"                     # Description de la commande "build"
	@echo "  run-app    Run the Flask application"                 # Description de la commande "run-app"
	@echo "  run-docker Run the Docker container"                  # Description de la commande "run-docker"
	@echo "  test       Run the unit tests"                        # Description de la commande "test"
	@echo "  test-api   Test the API endpoints"                    # Description de la commande "test-api"

# Commande "init" : crée un environnement virtuel Python
init:
	@echo "Setting up the virtual environment..."  # Message indiquant que l'environnement virtuel est en cours de création
	python3 -m venv .venv  # Crée un environnement virtuel dans le dossier .venv

# Commande "install" : installe les dépendances du projet après avoir exécuté "init"
install: init  # La commande "install" dépend de "init", donc init sera exécutée avant
	@echo "Installing dependencies..."  # Message indiquant que l'installation des dépendances commence
	. .venv/bin/activate && pip install -r requirements.txt  # Active l'environnement virtuel et installe les dépendances

# Commande "build" : construit l'image Docker pour le projet
build:
	@echo "Building the Docker image..."  # Message indiquant la construction de l'image Docker
	docker build -t health-calculator-service .  # Crée une image Docker avec le nom "health-calculator-service"

# Commande "run-docker" : exécute le conteneur Docker en arrière-plan
run-docker:  
	@echo "Running the Docker container..."  # Message indiquant que le conteneur Docker est en cours d'exécution
	docker run -d -p 5005:5005 health-calculator-service  # Lance le conteneur Docker, exposant le port 5005

# Commande "run-app" : exécute l'application Flask en mode développement
run-app:
	@echo "Running the Flask app..."  # Message indiquant que l'application Flask est en cours d'exécution
	python app.py  # Lance l'application Flask en exécutant le fichier app.py

# Commande "test" : exécute les tests unitaires définis dans le fichier test.py
test:
	@echo "Running unit tests..."  # Message indiquant que les tests unitaires sont en cours d'exécution
	python -m unittest test.py  # Exécute les tests unitaires avec le module unittest

# Commande "test-api" : teste les endpoints de l'API via une requête GET
test-api:
	@echo "Testing API endpoints..."  # Message indiquant que les endpoints de l'API sont en cours de test
	curl -X GET http://localhost:5005/  # Effectue une requête GET sur l'API locale à l'adresse http://localhost:5005/
