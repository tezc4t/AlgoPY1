"""
Tests unitaires pour l'exercice iteratif_500.
"""

import unittest
from io import StringIO
import sys
from iteratif_500 import (afficher_jusqu_a_500, afficher_jusqu_a_limite, 
                           obtenir_liste_jusqu_a_limite, compter_jusqu_a_limite,
                           afficher_jusqu_a_limite_par_pas)


class TestObtenirListeJusquaLimite(unittest.TestCase):
    """Tests pour la fonction obtenir_liste_jusqu_a_limite()."""
    
    def test_liste_jusqu_a_1(self):
        """Liste jusqu'à 1."""
        result = obtenir_liste_jusqu_a_limite(1)
        self.assertEqual(result, [1])
    
    def test_liste_jusqu_a_5(self):
        """Liste jusqu'à 5."""
        result = obtenir_liste_jusqu_a_limite(5)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_liste_jusqu_a_10(self):
        """Liste jusqu'à 10."""
        result = obtenir_liste_jusqu_a_limite(10)
        self.assertEqual(result, list(range(1, 11)))
    
    def test_liste_jusqu_a_500(self):
        """Liste jusqu'à 500."""
        result = obtenir_liste_jusqu_a_limite(500)
        self.assertEqual(len(result), 500)
        self.assertEqual(result[0], 1)
        self.assertEqual(result[-1], 500)
    
    def test_longueur_liste(self):
        """Vérifie que la longueur correspond à la limite."""
        for limite in [10, 50, 100, 500]:
            result = obtenir_liste_jusqu_a_limite(limite)
            self.assertEqual(len(result), limite)
    
    def test_liste_vide_limite_0(self):
        """Liste pour limite 0 devrait être vide."""
        result = obtenir_liste_jusqu_a_limite(0)
        self.assertEqual(result, [])


class TestCompterJusquaLimite(unittest.TestCase):
    """Tests pour la fonction compter_jusqu_a_limite()."""
    
    def test_compter_jusqu_a_1(self):
        """Compte jusqu'à 1."""
        result = compter_jusqu_a_limite(1)
        self.assertEqual(result, 1)
    
    def test_compter_jusqu_a_10(self):
        """Compte jusqu'à 10."""
        result = compter_jusqu_a_limite(10)
        self.assertEqual(result, 10)
    
    def test_compter_jusqu_a_500(self):
        """Compte jusqu'à 500."""
        result = compter_jusqu_a_limite(500)
        self.assertEqual(result, 500)
    
    def test_compter_jusqu_a_1000(self):
        """Compte jusqu'à 1000."""
        result = compter_jusqu_a_limite(1000)
        self.assertEqual(result, 1000)
    
    def test_compte_egale_limite(self):
        """Le compte doit être égal à la limite."""
        for limite in [5, 20, 100, 500]:
            result = compter_jusqu_a_limite(limite)
            self.assertEqual(result, limite)


class TestAfficherJusquaLimite(unittest.TestCase):
    """Tests pour la fonction afficher_jusqu_a_limite()."""
    
    def test_affiche_jusqu_a_5(self):
        """Affiche jusqu'à 5."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_jusqu_a_limite(5)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        self.assertEqual(len(lines), 5)
        self.assertEqual(lines[0], '1')
        self.assertEqual(lines[-1], '5')
    
    def test_affiche_jusqu_a_10(self):
        """Affiche jusqu'à 10."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_jusqu_a_limite(10)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        self.assertEqual(len(lines), 10)
        for i in range(10):
            self.assertEqual(lines[i], str(i + 1))
    
    def test_ne_depasse_pas_limite(self):
        """Vérifie que la limite n'est pas dépassée."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_jusqu_a_limite(20)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn('20', output)
        self.assertNotIn('21', output)


class TestAfficherJusqua500(unittest.TestCase):
    """Tests pour la fonction afficher_jusqu_a_500()."""
    
    def test_affiche_500_nombres(self):
        """Vérifie que 500 nombres sont affichés."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_jusqu_a_500()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        self.assertEqual(len(lines), 500)
    
    def test_commence_par_1(self):
        """Vérifie que l'affichage commence par 1."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_jusqu_a_500()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        self.assertEqual(lines[0], '1')
    
    def test_finit_par_500(self):
        """Vérifie que l'affichage finit par 500."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_jusqu_a_500()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        self.assertEqual(lines[-1], '500')
    
    def test_ne_depasse_pas_500(self):
        """Vérifie qu'on ne dépasse pas 500."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_jusqu_a_500()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn('500', output)
        self.assertNotIn('501', output)


class TestAfficherJusquaLimiteParPas(unittest.TestCase):
    """Tests pour la fonction afficher_jusqu_a_limite_par_pas()."""
    
    def test_pas_de_1(self):
        """Teste avec un pas de 1."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_jusqu_a_limite_par_pas(5, 1)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        self.assertEqual(lines, ['1', '2', '3', '4', '5'])
    
    def test_pas_de_5(self):
        """Teste avec un pas de 5."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_jusqu_a_limite_par_pas(20, 5)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        self.assertEqual(lines, ['1', '6', '11', '16'])
    
    def test_pas_de_10(self):
        """Teste avec un pas de 10."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        afficher_jusqu_a_limite_par_pas(50, 10)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        self.assertEqual(lines, ['1', '11', '21', '31', '41'])


class TestBoucleWhile(unittest.TestCase):
    """Tests pour vérifier l'utilisation de la boucle while."""
    
    def test_condition_ne_depasse_pas(self):
        """Vérifie que la condition while respecte la limite."""
        liste = obtenir_liste_jusqu_a_limite(100)
        
        # Aucun nombre ne doit dépasser 100
        for nombre in liste:
            self.assertLessEqual(nombre, 100)
    
    def test_iterativite(self):
        """Vérifie l'approche itérative."""
        # La liste doit contenir tous les nombres sans saut
        liste = obtenir_liste_jusqu_a_limite(20)
        
        for i in range(len(liste)):
            self.assertEqual(liste[i], i + 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
