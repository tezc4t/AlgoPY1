"""
Tests unitaires pour la fonction merge.
Teste la fusion de deux listes triées en une seule liste triée.
"""

import unittest
from merge_two_list import merge


class TestMerge(unittest.TestCase):
    """Tests pour la fonction merge()."""
    
    def test_merge_basic(self):
        """Fusionne deux listes triées simples."""
        result = merge([1, 2, 7, 8], [3, 4, 5, 6])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])
    
    def test_merge_equal_length(self):
        """Fusionne deux listes de même longueur."""
        result = merge([1, 3, 5], [2, 4, 6])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
    
    def test_merge_different_lengths(self):
        """Fusionne deux listes de longueurs différentes."""
        result = merge([1, 5, 9], [2, 3, 4, 6, 7, 8])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    def test_merge_first_all_smaller(self):
        """Première liste entièrement plus petite."""
        result = merge([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
    
    def test_merge_second_all_smaller(self):
        """Deuxième liste entièrement plus petite."""
        result = merge([4, 5, 6], [1, 2, 3])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
    
    def test_merge_with_duplicates(self):
        """Fusionne des listes avec des doublons."""
        result = merge([1, 3, 5, 5], [2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 3, 4, 5, 5, 5])
    
    def test_merge_identical_lists(self):
        """Fusionne deux listes identiques."""
        result = merge([1, 2, 3], [1, 2, 3])
        self.assertEqual(result, [1, 1, 2, 2, 3, 3])


class TestMergeEmptyLists(unittest.TestCase):
    """Tests avec des listes vides."""
    
    def test_merge_both_empty(self):
        """Fusionne deux listes vides."""
        result = merge([], [])
        self.assertEqual(result, [])
    
    def test_merge_first_empty(self):
        """Première liste vide."""
        result = merge([], [1, 2, 3])
        self.assertEqual(result, [1, 2, 3])
    
    def test_merge_second_empty(self):
        """Deuxième liste vide."""
        result = merge([1, 2, 3], [])
        self.assertEqual(result, [1, 2, 3])


class TestMergeSingleElement(unittest.TestCase):
    """Tests avec des listes à un seul élément."""
    
    def test_merge_both_single_element(self):
        """Deux listes à un élément."""
        result = merge([1], [2])
        self.assertEqual(result, [1, 2])
    
    def test_merge_both_single_element_reversed(self):
        """Deux listes à un élément (ordre inversé)."""
        result = merge([2], [1])
        self.assertEqual(result, [1, 2])
    
    def test_merge_both_single_element_same(self):
        """Deux listes à un élément identique."""
        result = merge([5], [5])
        self.assertEqual(result, [5, 5])
    
    def test_merge_single_with_multiple(self):
        """Liste à un élément avec liste multiple."""
        result = merge([3], [1, 2, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])


class TestMergeNegativeNumbers(unittest.TestCase):
    """Tests avec des nombres négatifs."""
    
    def test_merge_negative_numbers(self):
        """Fusionne des listes avec nombres négatifs."""
        result = merge([-5, -2, 0, 3], [-4, -1, 1, 4])
        self.assertEqual(result, [-5, -4, -2, -1, 0, 1, 3, 4])
    
    def test_merge_all_negative(self):
        """Fusionne des listes entièrement négatives."""
        result = merge([-10, -5, -1], [-8, -6, -2])
        self.assertEqual(result, [-10, -8, -6, -5, -2, -1])
    
    def test_merge_mixed_positive_negative(self):
        """Mélange de positifs et négatifs."""
        result = merge([-3, 0, 5], [-2, 1, 10])
        self.assertEqual(result, [-3, -2, 0, 1, 5, 10])


class TestMergeWithZero(unittest.TestCase):
    """Tests avec la valeur zéro."""
    
    def test_merge_with_zeros(self):
        """Fusionne des listes contenant des zéros."""
        result = merge([0, 2, 4], [0, 1, 3])
        self.assertEqual(result, [0, 0, 1, 2, 3, 4])
    
    def test_merge_only_zeros(self):
        """Fusionne des listes de zéros."""
        result = merge([0, 0, 0], [0, 0])
        self.assertEqual(result, [0, 0, 0, 0, 0])


class TestMergeLargeLists(unittest.TestCase):
    """Tests avec de grandes listes."""
    
    def test_merge_large_equal_lists(self):
        """Fusionne deux grandes listes égales."""
        list1 = list(range(0, 100, 2))  # [0, 2, 4, ..., 98]
        list2 = list(range(1, 100, 2))  # [1, 3, 5, ..., 99]
        result = merge(list1, list2)
        self.assertEqual(result, list(range(100)))
    
    def test_merge_large_different_sizes(self):
        """Fusionne une grande et une petite liste."""
        list1 = list(range(0, 1000, 2))
        list2 = [1, 3, 5]
        result = merge(list1, list2)
        self.assertEqual(len(result), 503)
        self.assertTrue(all(result[i] <= result[i+1] for i in range(len(result)-1)))
    
    def test_merge_very_large_lists(self):
        """Fusionne deux très grandes listes."""
        list1 = list(range(0, 10000, 2))
        list2 = list(range(1, 10000, 2))
        result = merge(list1, list2)
        self.assertEqual(len(result), 10000)
        self.assertEqual(result, list(range(10000)))


class TestMergeFloats(unittest.TestCase):
    """Tests avec des nombres à virgule."""
    
    def test_merge_floats(self):
        """Fusionne des listes de flottants."""
        result = merge([1.1, 2.5, 5.7], [1.3, 3.2, 4.8])
        self.assertEqual(result, [1.1, 1.3, 2.5, 3.2, 4.8, 5.7])
    
    def test_merge_mixed_int_float(self):
        """Fusionne des entiers et des flottants."""
        result = merge([1, 3, 5], [2.5, 4.5, 6.5])
        self.assertEqual(result, [1, 2.5, 3, 4.5, 5, 6.5])


class TestMergePreservesOrder(unittest.TestCase):
    """Tests pour vérifier que l'ordre est préservé."""
    
    def test_result_is_sorted(self):
        """Vérifie que le résultat est trié."""
        result = merge([1, 5, 9], [2, 6, 10])
        for i in range(len(result) - 1):
            self.assertLessEqual(result[i], result[i + 1])
    
    def test_stability_with_duplicates(self):
        """Vérifie la stabilité avec des doublons."""
        result = merge([1, 3, 5], [1, 3, 5])
        self.assertEqual(result, [1, 1, 3, 3, 5, 5])


class TestMergeReturnType(unittest.TestCase):
    """Tests du type de retour."""
    
    def test_returns_list(self):
        """Vérifie que la fonction retourne une liste."""
        result = merge([1, 2], [3, 4])
        self.assertIsInstance(result, list)
    
    def test_returns_new_list(self):
        """Vérifie que la fonction retourne une nouvelle liste."""
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        result = merge(list1, list2)
        
        # Modifier le résultat ne doit pas affecter les listes originales
        result.append(999)
        self.assertEqual(list1, [1, 2, 3])
        self.assertEqual(list2, [4, 5, 6])


class TestMergeCorrectness(unittest.TestCase):
    """Tests de vérification de la justesse."""
    
    def test_all_elements_included(self):
        """Vérifie que tous les éléments sont inclus."""
        list1 = [1, 3, 5, 7]
        list2 = [2, 4, 6, 8]
        result = merge(list1, list2)
        
        self.assertEqual(len(result), len(list1) + len(list2))
        
        for elem in list1:
            self.assertIn(elem, result)
        for elem in list2:
            self.assertIn(elem, result)
    
    def test_no_extra_elements(self):
        """Vérifie qu'aucun élément supplémentaire n'est ajouté."""
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        result = merge(list1, list2)
        
        self.assertEqual(sorted(result), sorted(list1 + list2))


class TestMergeEdgeCases(unittest.TestCase):
    """Tests des cas limites."""
    
    def test_merge_ascending_sequences(self):
        """Fusionne des séquences ascendantes."""
        result = merge([1, 2, 3], [10, 20, 30])
        self.assertEqual(result, [1, 2, 3, 10, 20, 30])
    
    def test_merge_descending_start_values(self):
        """Deuxième liste commence plus bas."""
        result = merge([10, 20, 30], [1, 2, 3])
        self.assertEqual(result, [1, 2, 3, 10, 20, 30])
    
    def test_merge_interleaved(self):
        """Listes parfaitement entrelacées."""
        result = merge([1, 3, 5, 7], [2, 4, 6, 8])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])
    
    def test_merge_one_element_each(self):
        """Une seule valeur dans chaque liste."""
        result = merge([100], [50])
        self.assertEqual(result, [50, 100])


if __name__ == '__main__':
    unittest.main(verbosity=2)
