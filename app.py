# Importe les modules nécessaires de Flask pour la gestion des requêtes et la génération de réponses JSON
from flask import Flask, render_template, request, jsonify
# Importe les fonctions de calcul BMI et BMR depuis le fichier health_utils
from health_utils import calculate_bmi, calculate_bmr

# Crée une instance de l'application Flask
app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/')
def home():
    # Rend le template 'index.html' lorsque l'utilisateur accède à la racine '/'
    return render_template('index.html')

# Route pour calculer le BMI (Body Mass Index), méthode POST
@app.route('/bmi', methods=['POST'])
def bmi():
    try:
        # Récupère les données du formulaire envoyées par la requête POST
        weight = float(request.form['weight'])  # Poids
        height = float(request.form['height'])  # Taille

        # Calcule le BMI en appelant la fonction correspondante dans health_utils
        bmi_result = calculate_bmi(weight, height)

        # Retourne le résultat du BMI sous forme de réponse JSON avec un code de statut 200 (OK)
        return jsonify({'bmi': bmi_result}), 200
    except (KeyError, ValueError) as e:
        # En cas d'erreur (mauvais format de données ou clé manquante), retourne une erreur 400 avec un message d'erreur
        return jsonify({'error': str(e)}), 400

# Route pour calculer le BMR (Basal Metabolic Rate), méthode POST
@app.route('/bmr', methods=['POST'])
def bmr():
    try:
        # Récupère les données du formulaire envoyées par la requête POST
        weight = float(request.form['weight'])  # Poids
        height = float(request.form['height'])  # Taille
        age = int(request.form['age'])  # Âge
        gender = request.form['gender']  # Sexe ('male' ou 'female')

        # Calcule le BMR en appelant la fonction correspondante dans health_utils
        bmr_result = calculate_bmr(weight, height, age, gender)

        # Retourne le résultat du BMR sous forme de réponse JSON avec un code de statut 200 (OK)
        return jsonify({'bmr': bmr_result}), 200
    except (KeyError, ValueError) as e:
        # En cas d'erreur (mauvais format de données ou clé manquante), retourne une erreur 400 avec un message d'erreur
        return jsonify({'error': str(e)}), 400

# Démarre l'application Flask lorsque ce script est exécuté directement
if __name__ == '__main__':
    app.run(port=5005, debug=True)  # L'application écoute sur le port 5005 et le mode debug est activé
