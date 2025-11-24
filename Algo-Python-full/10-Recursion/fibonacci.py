def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))  # Affiche 8

import unittest

"""
Tests unitaires pour la fonction fibonacci.
"""

class TestFibonacci(unittest.TestCase):
    """Classe de tests pour la fonction fibonacci."""

    def test_fibonacci_base(self):
        """Tests des cas de base : n = 0 et n = 1."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_petits_nombres(self):
        """Test avec de petits nombres."""
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_nombres_moyens(self):
        """Test avec des nombres moyens."""
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_entree_negative(self):
        """Test avec une entrée négative (devrait lever une RecursionError)."""
        with self.assertRaises(RecursionError):
            fibonacci(-1)
        with self.assertRaises(RecursionError):
            fibonacci(-5)


if __name__ == '__main__':
    unittest.main()
