def calculate_bmi(weight, height):
    """Calcule le Body Mass Index (BMI)."""
    
    # Vérifie si la hauteur ou le poids sont invalides (inférieurs ou égaux à 0)
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive values.")  # Lève une exception si l'une des valeurs est invalide
    
    # Calcule l'IMC en utilisant la formule : poids / (hauteur^2) et arrondit à 2 décimales
    return round(weight / (height ** 2), 2)

def calculate_bmr(weight, height, age, gender):
    """Calcule le Basal Metabolic Rate (BMR)."""
    
    # Vérifie que le poids, la taille et l'âge sont positifs et que le genre est valide
    if any(value <= 0 for value in [weight, height, age]) or gender not in ['male', 'female']:
        raise ValueError("Invalid input values.")  # Lève une exception si les valeurs sont invalides
    
    # Calcule le BMR en fonction du genre et des autres paramètres
    if gender == 'male':
        # Formule pour le BMR d'un homme
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:  # gender == 'female'
        # Formule pour le BMR d'une femme
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    # Retourne le BMR arrondi à 2 décimales
    return round(bmr, 2)
