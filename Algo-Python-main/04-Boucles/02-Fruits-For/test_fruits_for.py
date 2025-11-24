"""
Tests unitaires pour l'exercice fruits_for.
"""

import unittest
from io import StringIO
import sys
from fruits_for import afficher_fruits, afficher_fruits_numerotes, obtenir_fruits_liste


class TestObtenirFruitsListe(unittest.TestCase):
    """Tests pour la fonction obtenir_fruits_liste()."""
    
    def test_retourne_liste(self):
        """Vérifie que la fonction retourne une liste."""
        result = obtenir_fruits_liste()
        self.assertIsInstance(result, list)
    
    def test_contient_5_fruits(self):
        """Vérifie que la liste contient 5 fruits."""
        result = obtenir_fruits_liste()
        self.assertEqual(len(result), 5)
    
    def test_tous_elements_sont_strings(self):
        """Vérifie que tous les éléments sont des chaînes."""
        result = obtenir_fruits_liste()
        for fruit in result:
            self.assertIsInstance(fruit, str)
    
    def test_contenu_liste(self):
        """Vérifie le contenu de la liste."""
        result = obtenir_fruits_liste()
        expected = ["pomme", "banane", "orange", "fraise", "kiwi"]
        self.assertEqual(result, expected)


class TestAfficherFruits(unittest.TestCase):
    """Tests pour la fonction afficher_fruits()."""
    
    def test_affiche_un_fruit(self):
        """Affiche une liste avec un seul fruit."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_fruits(["pomme"])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("pomme", output)
    
    def test_affiche_cinq_fruits(self):
        """Affiche une liste avec cinq fruits."""
        fruits = ["pomme", "banane", "orange", "fraise", "kiwi"]
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_fruits(fruits)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        for fruit in fruits:
            self.assertIn(fruit, output)
    
    def test_affiche_ordre_correct(self):
        """Vérifie que l'ordre d'affichage est correct."""
        fruits = ["premier", "deuxieme", "troisieme"]
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_fruits(fruits)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        self.assertEqual(lines[0], "premier")
        self.assertEqual(lines[1], "deuxieme")
        self.assertEqual(lines[2], "troisieme")
    
    def test_liste_vide(self):
        """Teste avec une liste vide."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_fruits([])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output, "")


class TestAfficherFruitsNumerotes(unittest.TestCase):
    """Tests pour la fonction afficher_fruits_numerotes()."""
    
    def test_affiche_avec_numeros(self):
        """Vérifie que les fruits sont numérotés."""
        fruits = ["pomme", "banane", "orange"]
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_fruits_numerotes(fruits)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("1.", output)
        self.assertIn("2.", output)
        self.assertIn("3.", output)
    
    def test_numeros_commencent_a_1(self):
        """Vérifie que la numérotation commence à 1."""
        fruits = ["pomme"]
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_fruits_numerotes(fruits)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("1. pomme", output)
    
    def test_format_correct(self):
        """Vérifie le format d'affichage."""
        fruits = ["pomme", "banane"]
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_fruits_numerotes(fruits)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        self.assertEqual(lines[0], "1. pomme")
        self.assertEqual(lines[1], "2. banane")


class TestBoucleFor(unittest.TestCase):
    """Tests pour vérifier l'utilisation de la boucle for."""
    
    def test_parcourt_tous_elements(self):
        """Vérifie que tous les éléments sont parcourus."""
        fruits = ["a", "b", "c", "d", "e"]
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_fruits(fruits)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        self.assertEqual(len(lines), 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
