"""
Tests unitaires pour les exercices sur les variables locales et globales.
"""

import unittest
import sys
from io import StringIO
from variables_scope import set_local, modify_z


class TestVariablesLocales(unittest.TestCase):
    """Tests pour l'exercice sur les variables locales."""
    
    def test_set_local_execute_sans_erreur(self):
        """Vérifie que la fonction set_local s'exécute sans erreur."""
        try:
            set_local()
        except Exception as e:
            self.fail(f"set_local() a levé une exception : {e}")
    
    def test_set_local_affiche_valeur(self):
        """Vérifie que set_local affiche bien la valeur 15."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        set_local()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("15", output)
        self.assertIn("y", output.lower())
    
    def test_variable_locale_non_accessible(self):
        """Vérifie que la variable locale y n'est pas accessible hors de la fonction."""
        set_local()
        
        with self.assertRaises(NameError):
            # Cette ligne devrait lever une NameError
            _ = y  # noqa: F821


class TestVariablesGlobales(unittest.TestCase):
    """Tests pour l'exercice sur les variables globales."""
    
    def setUp(self):
        """Réinitialise z à 30 avant chaque test."""
        import variables_scope
        variables_scope.z = 30
    
    def test_z_initial_value(self):
        """Vérifie que z a bien la valeur initiale 30."""
        import variables_scope
        self.assertEqual(variables_scope.z, 30)
    
    def test_modify_z_change_value(self):
        """Vérifie que modify_z modifie bien z à 50."""
        import variables_scope
        
        self.assertEqual(variables_scope.z, 30)
        modify_z()
        self.assertEqual(variables_scope.z, 50)
    
    def test_modify_z_affiche_modification(self):
        """Vérifie que modify_z affiche la modification."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        modify_z()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("50", output)


if __name__ == '__main__':
    unittest.main()
