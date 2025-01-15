# Importation des modules nécessaires pour les tests unitaires
import unittest
# Importation des fonctions à tester depuis le module health_utils
from health_utils import calculate_bmi, calculate_bmr

# Définition de la classe de tests unitaires pour les fonctions de calcul
class TestHealthCalculatorUtils(unittest.TestCase):
    
    # Test de la fonction de calcul de l'IMC (Indice de Masse Corporelle)
    def test_calculate_bmi(self):
        # Test de l'IMC avec un poids de 80 kg et une taille de 1.80 mètre
        self.assertEqual(calculate_bmi(80, 1.80), 24.69)
        
        # Test pour vérifier que la fonction lève une exception ValueError pour un poids négatif
        with self.assertRaises(ValueError):
            calculate_bmi(-80, 1.80)
 
    # Test du calcul du BMR (Taux Métabolique de Base) pour un homme
    def test_calculate_bmr_male(self):
        # Test avec un poids de 80 kg, une taille de 180 cm, et un âge de 30 ans pour un homme
        self.assertEqual(calculate_bmr(80, 180, 30, 'male'), 1853.63)
 
    # Test du calcul du BMR pour une femme
    def test_calculate_bmr_female(self):
        # Test avec un poids de 80 kg, une taille de 180 cm, et un âge de 30 ans pour une femme
        self.assertEqual(calculate_bmr(80, 180, 30, 'female'), 1615.09)
 
    # Test pour vérifier que la fonction lève une exception ValueError pour un genre invalide
    def test_calculate_bmr_invalid(self):
        with self.assertRaises(ValueError):
            # Test avec un genre invalide (autre que 'male' ou 'female')
            calculate_bmr(80, 180, 30, 'other')

# Exécution des tests lorsque le fichier est exécuté directement
if __name__ == '__main__':
    unittest.main()
