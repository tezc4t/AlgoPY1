"""
Tests unitaires pour l'exercice nombres_1_n.
"""

import unittest
from io import StringIO
import sys
from nombres_1_n import afficher_1_a_n, obtenir_liste_1_a_n, afficher_1_a_n_sur_ligne, afficher_1_a_n_pairs_seulement


class TestObtenirListe1AN(unittest.TestCase):
    """Tests pour la fonction obtenir_liste_1_a_n()."""
    
    def test_liste_1_a_1(self):
        """Liste de 1 à 1."""
        result = obtenir_liste_1_a_n(1)
        self.assertEqual(result, [1])
    
    def test_liste_1_a_5(self):
        """Liste de 1 à 5."""
        result = obtenir_liste_1_a_n(5)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_liste_1_a_10(self):
        """Liste de 1 à 10."""
        result = obtenir_liste_1_a_n(10)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    def test_liste_vide_n_0(self):
        """Liste pour n=0 devrait être vide."""
        result = obtenir_liste_1_a_n(0)
        self.assertEqual(result, [])
    
    def test_longueur_liste(self):
        """Vérifie que la longueur de la liste est n."""
        for n in [1, 5, 10, 20, 100]:
            result = obtenir_liste_1_a_n(n)
            self.assertEqual(len(result), n)
    
    def test_premier_element_est_1(self):
        """Vérifie que le premier élément est 1."""
        result = obtenir_liste_1_a_n(10)
        self.assertEqual(result[0], 1)
    
    def test_dernier_element_est_n(self):
        """Vérifie que le dernier élément est n."""
        for n in [5, 10, 20]:
            result = obtenir_liste_1_a_n(n)
            self.assertEqual(result[-1], n)


class TestAfficher1AN(unittest.TestCase):
    """Tests pour la fonction afficher_1_a_n()."""
    
    def test_affiche_1_a_5(self):
        """Affiche les nombres de 1 à 5."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_1_a_n(5)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        self.assertEqual(len(lines), 5)
        self.assertEqual(lines[0], '1')
        self.assertEqual(lines[4], '5')
    
    def test_affiche_ordre_croissant(self):
        """Vérifie que les nombres sont affichés dans l'ordre croissant."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_1_a_n(10)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        for i in range(10):
            self.assertEqual(lines[i], str(i + 1))
    
    def test_affiche_tous_nombres(self):
        """Vérifie que tous les nombres sont affichés."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_1_a_n(3)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn('1', output)
        self.assertIn('2', output)
        self.assertIn('3', output)
    
    def test_n_1(self):
        """Teste avec n=1."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_1_a_n(1)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), '1')


class TestAfficher1ANSurLigne(unittest.TestCase):
    """Tests pour la fonction afficher_1_a_n_sur_ligne()."""
    
    def test_affiche_sur_une_ligne(self):
        """Vérifie que tous les nombres sont sur une seule ligne."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_1_a_n_sur_ligne(5)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        self.assertEqual(len(lines), 1)
    
    def test_contient_tous_nombres(self):
        """Vérifie que tous les nombres sont présents."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_1_a_n_sur_ligne(5)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        for i in range(1, 6):
            self.assertIn(str(i), output)


class TestAfficher1ANPairsSeulement(unittest.TestCase):
    """Tests pour la fonction afficher_1_a_n_pairs_seulement()."""
    
    def test_affiche_seulement_pairs(self):
        """Affiche seulement les nombres pairs."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_1_a_n_pairs_seulement(10)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        expected = ['2', '4', '6', '8', '10']
        self.assertEqual(lines, expected)
    
    def test_pas_de_nombres_impairs(self):
        """Vérifie qu'aucun nombre impair n'est affiché."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_1_a_n_pairs_seulement(10)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        # Vérifier que les nombres impairs ne sont pas présents
        self.assertNotIn('1\n', output)
        self.assertNotIn('3\n', output)
        self.assertNotIn('5\n', output)
        self.assertNotIn('7\n', output)
        self.assertNotIn('9\n', output)


class TestBoucleForRange(unittest.TestCase):
    """Tests pour vérifier l'utilisation correcte de range()."""
    
    def test_range_inclut_n(self):
        """Vérifie que n est inclus dans l'affichage."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_1_a_n(100)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn('100', output)
    
    def test_commence_a_1(self):
        """Vérifie que l'affichage commence à 1."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_1_a_n(10)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        self.assertEqual(lines[0], '1')


if __name__ == '__main__':
    unittest.main(verbosity=2)
