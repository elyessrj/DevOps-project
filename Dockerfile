# Utilise l'image officielle de Python 3.9 comme base pour l'image Docker
FROM python:3.9

# Définit le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copie tous les fichiers du répertoire local dans le répertoire de travail du conteneur
COPY . /app

# Installe les dépendances Python listées dans le fichier requirements.txt
RUN pip install -r requirements.txt

# Expose le port 5005 pour que l'application Flask puisse être accessible
EXPOSE 5005

# Définit la commande à exécuter lorsque le conteneur démarre : lance l'application Flask avec python
CMD ["python", "app.py"]
