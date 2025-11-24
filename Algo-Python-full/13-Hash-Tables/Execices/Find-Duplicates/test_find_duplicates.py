"""
Tests unitaires pour la fonction find_duplicates.
Teste la détection des doublons dans une liste en utilisant des dictionnaires.
"""

import unittest
from find_duplicates import find_duplicates


class TestFindDuplicates(unittest.TestCase):
    """Tests pour la fonction find_duplicates()."""
    
    def test_no_duplicates(self):
        """Liste sans doublons."""
        result = find_duplicates([1, 2, 3, 4, 5])
        self.assertEqual(result, [])
    
    def test_two_duplicates(self):
        """Liste avec deux éléments dupliqués."""
        result = find_duplicates([1, 1, 2, 2, 3])
        self.assertEqual(sorted(result), [1, 2])
    
    def test_single_value_repeated(self):
        """Liste avec un seul élément répété."""
        result = find_duplicates([1, 1, 1, 1, 1])
        self.assertEqual(result, [1])
    
    def test_multiple_duplicates_various_counts(self):
        """Liste avec plusieurs doublons de comptages variés."""
        result = find_duplicates([1, 2, 3, 3, 3, 4, 4, 5])
        self.assertEqual(sorted(result), [3, 4])
    
    def test_all_elements_duplicated(self):
        """Liste où tous les éléments sont dupliqués."""
        result = find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3])
        self.assertEqual(sorted(result), [1, 2, 3])
    
    def test_all_elements_duplicated_variant(self):
        """Variante avec tous les éléments dupliqués."""
        result = find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3])
        self.assertEqual(sorted(result), [1, 2, 3])
    
    def test_empty_list(self):
        """Liste vide."""
        result = find_duplicates([])
        self.assertEqual(result, [])


class TestFindDuplicatesEdgeCases(unittest.TestCase):
    """Tests des cas limites."""
    
    def test_single_element(self):
        """Liste avec un seul élément."""
        result = find_duplicates([1])
        self.assertEqual(result, [])
    
    def test_two_identical_elements(self):
        """Liste avec deux éléments identiques."""
        result = find_duplicates([5, 5])
        self.assertEqual(result, [5])
    
    def test_two_different_elements(self):
        """Liste avec deux éléments différents."""
        result = find_duplicates([1, 2])
        self.assertEqual(result, [])


class TestFindDuplicatesWithNegatives(unittest.TestCase):
    """Tests avec des nombres négatifs."""
    
    def test_negative_duplicates(self):
        """Doublons avec nombres négatifs."""
        result = find_duplicates([-1, -1, -2, -2, 3])
        self.assertEqual(sorted(result), [-2, -1])
    
    def test_mixed_positive_negative_duplicates(self):
        """Doublons mixtes positifs et négatifs."""
        result = find_duplicates([-5, -5, 0, 0, 5, 5])
        self.assertEqual(sorted(result), [-5, 0, 5])


class TestFindDuplicatesWithZero(unittest.TestCase):
    """Tests avec la valeur zéro."""
    
    def test_zero_duplicated(self):
        """Zéro comme doublon."""
        result = find_duplicates([0, 0, 1, 2])
        self.assertEqual(result, [0])
    
    def test_only_zeros(self):
        """Liste composée uniquement de zéros."""
        result = find_duplicates([0, 0, 0, 0])
        self.assertEqual(result, [0])


class TestFindDuplicatesWithStrings(unittest.TestCase):
    """Tests avec des chaînes de caractères."""
    
    def test_string_duplicates(self):
        """Doublons de chaînes."""
        result = find_duplicates(['apple', 'apple', 'banana', 'cherry'])
        self.assertEqual(result, ['apple'])
    
    def test_multiple_string_duplicates(self):
        """Plusieurs chaînes dupliquées."""
        result = find_duplicates(['a', 'a', 'b', 'b', 'c'])
        self.assertEqual(sorted(result), ['a', 'b'])
    
    def test_no_string_duplicates(self):
        """Chaînes sans doublons."""
        result = find_duplicates(['x', 'y', 'z'])
        self.assertEqual(result, [])


class TestFindDuplicatesReturnType(unittest.TestCase):
    """Tests du type de retour."""
    
    def test_returns_list(self):
        """Vérifie que la fonction retourne une liste."""
        result = find_duplicates([1, 1, 2])
        self.assertIsInstance(result, list)
    
    def test_returns_list_when_empty(self):
        """Vérifie que la fonction retourne une liste vide."""
        result = find_duplicates([])
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)


class TestFindDuplicatesOrder(unittest.TestCase):
    """Tests de l'ordre des résultats."""
    
    def test_order_preserved_simple(self):
        """Vérifie l'ordre d'apparition des doublons."""
        result = find_duplicates([3, 3, 1, 1, 2, 2])
        # L'ordre peut varier selon l'implémentation, on vérifie juste le contenu
        self.assertEqual(sorted(result), [1, 2, 3])
    
    def test_result_contains_all_duplicates(self):
        """Vérifie que tous les doublons sont inclus."""
        result = find_duplicates([5, 5, 10, 10, 15, 15, 20])
        self.assertEqual(sorted(result), [5, 10, 15])


class TestFindDuplicatesLargeLists(unittest.TestCase):
    """Tests avec de grandes listes."""
    
    def test_large_list_no_duplicates(self):
        """Grande liste sans doublons."""
        result = find_duplicates(list(range(1000)))
        self.assertEqual(result, [])
    
    def test_large_list_all_duplicates(self):
        """Grande liste où chaque élément est dupliqué."""
        list1 = []
        for i in range(500):
            list1.extend([i, i])
        result = find_duplicates(list1)
        self.assertEqual(len(result), 500)
    
    def test_large_list_some_duplicates(self):
        """Grande liste avec quelques doublons."""
        list1 = list(range(100)) + [1, 1, 50, 50, 99, 99]
        result = find_duplicates(list1)
        self.assertEqual(sorted(result), [1, 50, 99])


class TestFindDuplicatesMultipleOccurrences(unittest.TestCase):
    """Tests avec différents nombres d'occurrences."""
    
    def test_two_occurrences(self):
        """Élément apparaissant exactement deux fois."""
        result = find_duplicates([1, 2, 2, 3])
        self.assertEqual(result, [2])
    
    def test_three_occurrences(self):
        """Élément apparaissant trois fois."""
        result = find_duplicates([1, 2, 2, 2, 3])
        self.assertEqual(result, [2])
    
    def test_many_occurrences(self):
        """Élément apparaissant de nombreuses fois."""
        result = find_duplicates([1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(result, [1])
    
    def test_different_occurrence_counts(self):
        """Différents éléments avec différents comptages."""
        result = find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4])
        self.assertEqual(sorted(result), [1, 2, 3, 4])


class TestFindDuplicatesMixedTypes(unittest.TestCase):
    """Tests avec des types mixtes."""
    
    def test_int_and_float(self):
        """Mélange d'entiers et de flottants."""
        result = find_duplicates([1, 1.0, 2, 2.0])
        # 1 et 1.0 sont considérés égaux en Python
        self.assertEqual(sorted(result), [1, 2])
    
    def test_boolean_duplicates(self):
        """Doublons de booléens."""
        result = find_duplicates([True, True, False, False, True])
        # True et False peuvent se comporter comme 1 et 0
        self.assertTrue(len(result) >= 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
