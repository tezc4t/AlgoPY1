"""
Tests unitaires pour les fonctions arithmétiques.
"""

import unittest
from addition import addition, quotient, modulo


class TestAddition(unittest.TestCase):
    """Classe de tests pour la fonction addition."""
    
    def test_addition_nombres_positifs(self):
        """Test avec deux nombres positifs."""
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(10, 20), 30)
    
    def test_addition_nombres_negatifs(self):
        """Test avec deux nombres négatifs."""
        self.assertEqual(addition(-5, -3), -8)
        self.assertEqual(addition(-10, -1), -11)
    
    def test_addition_mixte(self):
        """Test avec un nombre positif et un nombre négatif."""
        self.assertEqual(addition(5, -3), 2)
        self.assertEqual(addition(-5, 3), -2)
    
    def test_addition_avec_zero(self):
        """Test avec zéro."""
        self.assertEqual(addition(0, 5), 5)
        self.assertEqual(addition(5, 0), 5)
        self.assertEqual(addition(0, 0), 0)
    
    def test_addition_nombres_decimaux(self):
        """Test avec des nombres décimaux."""
        self.assertAlmostEqual(addition(2.5, 3.7), 6.2)
        self.assertAlmostEqual(addition(1.1, 2.2), 3.3)
    
    def test_addition_grands_nombres(self):
        """Test avec de grands nombres."""
        self.assertEqual(addition(1000000, 2000000), 3000000)


class TestQuotient(unittest.TestCase):
    """Classe de tests pour la fonction quotient."""
    
    def test_quotient_division_exacte(self):
        """Test avec une division exacte."""
        self.assertEqual(quotient(10, 2), 5)
        self.assertEqual(quotient(20, 4), 5)
    
    def test_quotient_division_avec_reste(self):
        """Test avec une division avec reste."""
        self.assertEqual(quotient(10, 3), 3)
        self.assertEqual(quotient(15, 4), 3)
        self.assertEqual(quotient(7, 2), 3)
    
    def test_quotient_dividende_plus_petit(self):
        """Test quand le dividende est plus petit que le diviseur."""
        self.assertEqual(quotient(3, 5), 0)
        self.assertEqual(quotient(1, 10), 0)
    
    def test_quotient_nombres_negatifs(self):
        """Test avec des nombres négatifs."""
        self.assertEqual(quotient(-10, 3), -4)
        self.assertEqual(quotient(10, -3), -4)
        self.assertEqual(quotient(-10, -3), 3)
    
    def test_quotient_division_par_zero(self):
        """Test de la division par zéro."""
        with self.assertRaises(ZeroDivisionError):
            quotient(10, 0)


class TestModulo(unittest.TestCase):
    """Classe de tests pour la fonction modulo."""
    
    def test_modulo_division_avec_reste(self):
        """Test du reste d'une division."""
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(15, 4), 3)
        self.assertEqual(modulo(7, 2), 1)
    
    def test_modulo_division_exacte(self):
        """Test quand la division est exacte (reste = 0)."""
        self.assertEqual(modulo(10, 2), 0)
        self.assertEqual(modulo(20, 4), 0)
    
    def test_modulo_dividende_plus_petit(self):
        """Test quand le dividende est plus petit que le diviseur."""
        self.assertEqual(modulo(3, 5), 3)
        self.assertEqual(modulo(1, 10), 1)
    
    def test_modulo_nombres_negatifs(self):
        """Test avec des nombres négatifs."""
        self.assertEqual(modulo(-10, 3), 2)
        self.assertEqual(modulo(10, -3), -2)
    
    def test_modulo_division_par_zero(self):
        """Test de la division par zéro."""
        with self.assertRaises(ZeroDivisionError):
            modulo(10, 0)


if __name__ == '__main__':
    unittest.main()
