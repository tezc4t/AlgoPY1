def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(4))

import unittest

"""
Tests unitaires pour la fonction factorial.
"""



class TestFactorial(unittest.TestCase):
    """Classe de tests pour la fonction factorial."""
    
    def test_factorial_un(self):
        """Test avec n = 1 (cas de base)."""
        self.assertEqual(factorial(1), 1)
    
    def test_factorial_petits_nombres(self):
        """Test avec de petits nombres."""
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
    
    def test_factorial_nombres_moyens(self):
        """Test avec des nombres moyens."""
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(10), 3628800)
    
    def test_factorial_zero(self):
        """Test avec n = 0 (devrait causer une erreur avec l'implémentation actuelle)."""
        with self.assertRaises(RecursionError):
            factorial(0)
    
    def test_factorial_nombre_negatif(self):
        """Test avec un nombre négatif (devrait causer une erreur)."""
        with self.assertRaises(RecursionError):
            factorial(-1)
        with self.assertRaises(RecursionError):
            factorial(-5)


if __name__ == '__main__':
    unittest.main()