"""
Tests unitaires pour l'exercice somme_while.
"""

import unittest
from somme_while import somme_1_a_100, somme_1_a_n


class TestSomme1A100(unittest.TestCase):
    """Tests pour la fonction somme_1_a_100()."""
    
    def test_somme_1_a_100(self):
        """Vérifie que la somme de 1 à 100 est correcte."""
        result = somme_1_a_100()
        self.assertEqual(result, 5050)
    
    def test_somme_1_a_100_type(self):
        """Vérifie que le résultat est un entier."""
        result = somme_1_a_100()
        self.assertIsInstance(result, int)


class TestSomme1AN(unittest.TestCase):
    """Tests pour la fonction somme_1_a_n()."""
    
    def test_somme_1_a_1(self):
        """Somme de 1 à 1."""
        self.assertEqual(somme_1_a_n(1), 1)
    
    def test_somme_1_a_5(self):
        """Somme de 1 à 5 = 1+2+3+4+5 = 15."""
        self.assertEqual(somme_1_a_n(5), 15)
    
    def test_somme_1_a_10(self):
        """Somme de 1 à 10 = 55."""
        self.assertEqual(somme_1_a_n(10), 55)
    
    def test_somme_1_a_50(self):
        """Somme de 1 à 50 = 1275."""
        self.assertEqual(somme_1_a_n(50), 1275)
    
    def test_somme_1_a_100(self):
        """Somme de 1 à 100 = 5050."""
        self.assertEqual(somme_1_a_n(100), 5050)
    
    def test_somme_1_a_0(self):
        """Somme de 1 à 0 devrait être 0."""
        self.assertEqual(somme_1_a_n(0), 0)
    
    def test_somme_formule_mathematique(self):
        """Vérifie que le résultat correspond à la formule n*(n+1)/2."""
        for n in [1, 5, 10, 20, 50, 100]:
            expected = n * (n + 1) // 2
            self.assertEqual(somme_1_a_n(n), expected)
    
    def test_somme_1_a_1000(self):
        """Somme de 1 à 1000 = 500500."""
        self.assertEqual(somme_1_a_n(1000), 500500)


if __name__ == '__main__':
    unittest.main(verbosity=2)
