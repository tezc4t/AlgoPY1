"""
Tests unitaires pour la fonction reverse_string utilisant une Stack.
Teste l'inversion de chaînes de caractères avec une pile.
"""

import unittest
import sys
import os

# Ajouter le chemin du dossier parent pour importer StackArray
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from reverse_string import reverse_string


class TestReverseString(unittest.TestCase):
    """Tests pour la fonction reverse_string()."""
    
    def test_reverse_simple_string(self):
        """Inverse une chaîne simple."""
        result = reverse_string('hello')
        self.assertEqual(result, 'olleh')
    
    def test_reverse_single_character(self):
        """Inverse une chaîne d'un seul caractère."""
        result = reverse_string('a')
        self.assertEqual(result, 'a')
    
    def test_reverse_empty_string(self):
        """Inverse une chaîne vide."""
        result = reverse_string('')
        self.assertEqual(result, '')
    
    def test_reverse_two_characters(self):
        """Inverse une chaîne de deux caractères."""
        result = reverse_string('ab')
        self.assertEqual(result, 'ba')
    
    def test_reverse_palindrome(self):
        """Inverse un palindrome."""
        result = reverse_string('radar')
        self.assertEqual(result, 'radar')
    
    def test_reverse_with_spaces(self):
        """Inverse une chaîne avec des espaces."""
        result = reverse_string('hello world')
        self.assertEqual(result, 'dlrow olleh')
    
    def test_reverse_with_numbers(self):
        """Inverse une chaîne avec des chiffres."""
        result = reverse_string('abc123')
        self.assertEqual(result, '321cba')
    
    def test_reverse_with_special_characters(self):
        """Inverse une chaîne avec des caractères spéciaux."""
        result = reverse_string('hello!')
        self.assertEqual(result, '!olleh')
    
    def test_reverse_with_mixed_case(self):
        """Inverse une chaîne avec majuscules et minuscules."""
        result = reverse_string('HeLLo')
        self.assertEqual(result, 'oLLeH')
    
    def test_reverse_long_string(self):
        """Inverse une chaîne longue."""
        result = reverse_string('abcdefghijklmnopqrstuvwxyz')
        self.assertEqual(result, 'zyxwvutsrqponmlkjihgfedcba')
    
    def test_reverse_with_punctuation(self):
        """Inverse une chaîne avec ponctuation."""
        result = reverse_string('Hello, World!')
        self.assertEqual(result, '!dlroW ,olleH')
    





if __name__ == '__main__':
    unittest.main(verbosity=2)
