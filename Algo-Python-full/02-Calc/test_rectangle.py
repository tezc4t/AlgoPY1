"""
Tests unitaires pour les fonctions de calcul de rectangle.
"""

import unittest
from rectangle import aire_rectangle, perimetre_rectangle


class TestAireRectangle(unittest.TestCase):
    """Classe de tests pour la fonction aire_rectangle."""
    
    def test_aire_nombres_entiers(self):
        """Test avec des nombres entiers."""
        self.assertEqual(aire_rectangle(5, 3), 15)
        self.assertEqual(aire_rectangle(10, 10), 100)
        self.assertEqual(aire_rectangle(7, 4), 28)
    
    def test_aire_nombres_decimaux(self):
        """Test avec des nombres décimaux."""
        self.assertAlmostEqual(aire_rectangle(5.5, 2.0), 11.0)
        self.assertAlmostEqual(aire_rectangle(3.2, 4.5), 14.4)
    
    def test_aire_avec_zero(self):
        """Test avec zéro."""
        self.assertEqual(aire_rectangle(0, 5), 0)
        self.assertEqual(aire_rectangle(5, 0), 0)
        self.assertEqual(aire_rectangle(0, 0), 0)
    
    def test_aire_grands_nombres(self):
        """Test avec de grands nombres."""
        self.assertEqual(aire_rectangle(1000, 500), 500000)
    
    def test_aire_petits_nombres(self):
        """Test avec de petits nombres."""
        self.assertAlmostEqual(aire_rectangle(0.1, 0.2), 0.02)


class TestPerimetreRectangle(unittest.TestCase):
    """Classe de tests pour la fonction perimetre_rectangle."""
    
    def test_perimetre_nombres_entiers(self):
        """Test avec des nombres entiers."""
        self.assertEqual(perimetre_rectangle(5, 3), 16)
        self.assertEqual(perimetre_rectangle(10, 10), 40)
        self.assertEqual(perimetre_rectangle(7, 4), 22)
    
    def test_perimetre_nombres_decimaux(self):
        """Test avec des nombres décimaux."""
        self.assertAlmostEqual(perimetre_rectangle(5.5, 2.0), 15.0)
        self.assertAlmostEqual(perimetre_rectangle(3.2, 4.5), 15.4)
    
    def test_perimetre_avec_zero(self):
        """Test avec zéro."""
        self.assertEqual(perimetre_rectangle(0, 5), 10)
        self.assertEqual(perimetre_rectangle(5, 0), 10)
        self.assertEqual(perimetre_rectangle(0, 0), 0)
    
    def test_perimetre_carre(self):
        """Test avec un carré (longueur = largeur)."""
        self.assertEqual(perimetre_rectangle(5, 5), 20)
        self.assertEqual(perimetre_rectangle(8, 8), 32)


if __name__ == '__main__':
    unittest.main()
