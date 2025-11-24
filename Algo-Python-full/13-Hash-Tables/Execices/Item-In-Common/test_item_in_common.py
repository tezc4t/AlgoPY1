"""
Tests unitaires pour la fonction item_in_common.
Teste la détection d'éléments communs entre deux listes en utilisant un dictionnaire.
"""

import unittest
from item_in_common import item_in_common


class TestItemInCommon(unittest.TestCase):
    """Tests pour la fonction item_in_common()."""
    
    def test_has_common_item(self):
        """Vérifie la détection d'un élément commun."""
        list1 = [1, 3, 5]
        list2 = [2, 4, 5]
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_no_common_item(self):
        """Vérifie l'absence d'élément commun."""
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        
        self.assertFalse(item_in_common(list1, list2))
    
    def test_multiple_common_items(self):
        """Vérifie avec plusieurs éléments communs."""
        list1 = [1, 2, 3, 4, 5]
        list2 = [3, 4, 5, 6, 7]
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_all_items_common(self):
        """Vérifie quand toutes les valeurs sont communes."""
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_single_common_item(self):
        """Vérifie avec un seul élément commun."""
        list1 = [1, 2, 3, 4, 5]
        list2 = [6, 7, 8, 9, 3]
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_empty_first_list(self):
        """Vérifie avec la première liste vide."""
        list1 = []
        list2 = [1, 2, 3]
        
        self.assertFalse(item_in_common(list1, list2))
    
    def test_empty_second_list(self):
        """Vérifie avec la deuxième liste vide."""
        list1 = [1, 2, 3]
        list2 = []
        
        self.assertFalse(item_in_common(list1, list2))
    
    def test_both_empty_lists(self):
        """Vérifie avec les deux listes vides."""
        list1 = []
        list2 = []
        
        self.assertFalse(item_in_common(list1, list2))
    
    def test_single_element_each_same(self):
        """Vérifie avec un élément identique dans chaque liste."""
        list1 = [5]
        list2 = [5]
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_single_element_each_different(self):
        """Vérifie avec un élément différent dans chaque liste."""
        list1 = [5]
        list2 = [10]
        
        self.assertFalse(item_in_common(list1, list2))


class TestItemInCommonWithStrings(unittest.TestCase):
    """Tests avec des chaînes de caractères."""
    
    def test_common_strings(self):
        """Vérifie avec des chaînes communes."""
        list1 = ['apple', 'banana', 'cherry']
        list2 = ['orange', 'banana', 'grape']
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_no_common_strings(self):
        """Vérifie avec des chaînes sans élément commun."""
        list1 = ['apple', 'banana']
        list2 = ['orange', 'grape']
        
        self.assertFalse(item_in_common(list1, list2))
    
    def test_case_sensitive_strings(self):
        """Vérifie la sensibilité à la casse."""
        list1 = ['Apple', 'Banana']
        list2 = ['apple', 'banana']
        
        self.assertFalse(item_in_common(list1, list2))
    
    def test_empty_strings(self):
        """Vérifie avec des chaînes vides."""
        list1 = ['', 'test']
        list2 = ['', 'other']
        
        self.assertTrue(item_in_common(list1, list2))


class TestItemInCommonWithNegatives(unittest.TestCase):
    """Tests avec des nombres négatifs."""
    
    def test_negative_numbers_common(self):
        """Vérifie avec des nombres négatifs communs."""
        list1 = [-1, -2, -3]
        list2 = [1, 2, -2]
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_negative_numbers_no_common(self):
        """Vérifie avec des nombres négatifs sans élément commun."""
        list1 = [-1, -2, -3]
        list2 = [1, 2, 3]
        
        self.assertFalse(item_in_common(list1, list2))
    
    def test_mixed_positive_negative(self):
        """Vérifie avec un mélange de positifs et négatifs."""
        list1 = [-5, 0, 5]
        list2 = [10, 0, -10]
        
        self.assertTrue(item_in_common(list1, list2))


class TestItemInCommonWithZero(unittest.TestCase):
    """Tests avec la valeur zéro."""
    
    def test_zero_in_common(self):
        """Vérifie avec zéro comme élément commun."""
        list1 = [0, 1, 2]
        list2 = [3, 0, 4]
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_only_zeros(self):
        """Vérifie avec uniquement des zéros."""
        list1 = [0, 0, 0]
        list2 = [0, 0, 0]
        
        self.assertTrue(item_in_common(list1, list2))


class TestItemInCommonWithDuplicates(unittest.TestCase):
    """Tests avec des doublons dans les listes."""
    
    def test_duplicates_in_first_list(self):
        """Vérifie avec des doublons dans la première liste."""
        list1 = [1, 1, 2, 2, 3, 3]
        list2 = [4, 5, 3]
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_duplicates_in_second_list(self):
        """Vérifie avec des doublons dans la deuxième liste."""
        list1 = [1, 2, 3]
        list2 = [4, 4, 5, 5, 3, 3]
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_duplicates_in_both_lists(self):
        """Vérifie avec des doublons dans les deux listes."""
        list1 = [1, 1, 2, 2]
        list2 = [2, 2, 3, 3]
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_no_common_with_duplicates(self):
        """Vérifie sans élément commun malgré les doublons."""
        list1 = [1, 1, 2, 2]
        list2 = [3, 3, 4, 4]
        
        self.assertFalse(item_in_common(list1, list2))


class TestItemInCommonWithMixedTypes(unittest.TestCase):
    """Tests avec des types mixtes."""
    
    def test_mixed_int_float(self):
        """Vérifie avec des entiers et des flottants."""
        list1 = [1, 2.5, 3]
        list2 = [4, 2.5, 5]
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_mixed_types_no_common(self):
        """Vérifie avec types mixtes sans élément commun."""
        list1 = [1, 2, 3]
        list2 = ['1', '2', '3']
        
        self.assertFalse(item_in_common(list1, list2))
    
    def test_int_and_float_equality(self):
        """Vérifie l'égalité entre int et float (1 == 1.0)."""
        list1 = [1, 2, 3]
        list2 = [4, 5, 1.0]
        
        self.assertTrue(item_in_common(list1, list2))


class TestItemInCommonPerformance(unittest.TestCase):
    """Tests de performance avec de grandes listes."""
    
    def test_large_lists_with_common(self):
        """Vérifie avec de grandes listes ayant un élément commun."""
        list1 = list(range(1000))
        list2 = list(range(500, 1500))
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_large_lists_no_common(self):
        """Vérifie avec de grandes listes sans élément commun."""
        list1 = list(range(1000))
        list2 = list(range(1000, 2000))
        
        self.assertFalse(item_in_common(list1, list2))
    
    def test_common_at_end(self):
        """Vérifie quand l'élément commun est à la fin."""
        list1 = list(range(100))
        list2 = [1000, 1001, 1002, 99]
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_common_at_start(self):
        """Vérifie quand l'élément commun est au début."""
        list1 = list(range(100))
        list2 = [0, 1000, 1001, 1002]
        
        self.assertTrue(item_in_common(list1, list2))


class TestItemInCommonEdgeCases(unittest.TestCase):
    """Tests des cas limites."""
    
    def test_very_long_first_list(self):
        """Vérifie avec une première liste très longue."""
        list1 = list(range(10000))
        list2 = [5000]
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_very_long_second_list(self):
        """Vérifie avec une deuxième liste très longue."""
        list1 = [5000]
        list2 = list(range(10000))
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_single_vs_multiple(self):
        """Vérifie une liste à un élément vs liste multiple."""
        list1 = [42]
        list2 = [1, 2, 3, 42, 5, 6]
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_boolean_values(self):
        """Vérifie avec des valeurs booléennes."""
        list1 = [True, False]
        list2 = [False, 1, 2]
        
        self.assertTrue(item_in_common(list1, list2))
    
    def test_none_value(self):
        """Vérifie avec None comme valeur."""
        list1 = [1, None, 3]
        list2 = [4, None, 5]
        
        self.assertTrue(item_in_common(list1, list2))


class TestItemInCommonReturnType(unittest.TestCase):
    """Tests du type de retour."""
    
    def test_returns_boolean_true(self):
        """Vérifie que la fonction retourne un booléen True."""
        result = item_in_common([1, 2], [2, 3])
        self.assertIsInstance(result, bool)
        self.assertTrue(result)
    
    def test_returns_boolean_false(self):
        """Vérifie que la fonction retourne un booléen False."""
        result = item_in_common([1, 2], [3, 4])
        self.assertIsInstance(result, bool)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
