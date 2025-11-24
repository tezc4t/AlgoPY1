"""
Tests unitaires pour la fonction merge_sort.
Teste l'algorithme de tri par fusion (merge sort).
"""

import unittest
from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    """Tests pour la fonction merge_sort()."""
    
    def test_sort_basic(self):
        """Trie une liste simple."""
        result = merge_sort([3, 1, 4, 2])
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_sort_already_sorted(self):
        """Trie une liste déjà triée."""
        result = merge_sort([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_sort_reverse_sorted(self):
        """Trie une liste triée en ordre inverse."""
        result = merge_sort([5, 4, 3, 2, 1])
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_sort_with_duplicates(self):
        """Trie une liste avec des doublons."""
        result = merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5])
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 5, 6, 9])
    
    def test_sort_all_same(self):
        """Trie une liste où tous les éléments sont identiques."""
        result = merge_sort([5, 5, 5, 5, 5])
        self.assertEqual(result, [5, 5, 5, 5, 5])
    
    def test_sort_single_element(self):
        """Trie une liste à un seul élément."""
        result = merge_sort([42])
        self.assertEqual(result, [42])
    
    def test_sort_two_elements_sorted(self):
        """Trie deux éléments déjà triés."""
        result = merge_sort([1, 2])
        self.assertEqual(result, [1, 2])
    
    def test_sort_two_elements_unsorted(self):
        """Trie deux éléments non triés."""
        result = merge_sort([2, 1])
        self.assertEqual(result, [1, 2])


class TestMergeSortNegativeNumbers(unittest.TestCase):
    """Tests avec des nombres négatifs."""
    
    def test_sort_negative_numbers(self):
        """Trie une liste avec des nombres négatifs."""
        result = merge_sort([-3, 5, -1, 0, 2, -4])
        self.assertEqual(result, [-4, -3, -1, 0, 2, 5])
    
    def test_sort_all_negative(self):
        """Trie une liste entièrement négative."""
        result = merge_sort([-10, -5, -20, -1, -15])
        self.assertEqual(result, [-20, -15, -10, -5, -1])
    
    def test_sort_mixed_positive_negative(self):
        """Trie un mélange de positifs et négatifs."""
        result = merge_sort([3, -2, 0, 5, -5, 1])
        self.assertEqual(result, [-5, -2, 0, 1, 3, 5])


class TestMergeSortWithZero(unittest.TestCase):
    """Tests avec la valeur zéro."""
    
    def test_sort_with_zeros(self):
        """Trie une liste contenant des zéros."""
        result = merge_sort([0, 3, 0, 1, 0, 2])
        self.assertEqual(result, [0, 0, 0, 1, 2, 3])
    
    def test_sort_only_zeros(self):
        """Trie une liste de zéros."""
        result = merge_sort([0, 0, 0, 0])
        self.assertEqual(result, [0, 0, 0, 0])


class TestMergeSortLargeLists(unittest.TestCase):
    """Tests avec de grandes listes."""
    
    def test_sort_large_random_list(self):
        """Trie une grande liste."""
        import random
        original = [random.randint(1, 1000) for _ in range(100)]
        result = merge_sort(original)
        expected = sorted(original)
        self.assertEqual(result, expected)
    
    def test_sort_large_sorted_list(self):
        """Trie une grande liste déjà triée."""
        original = list(range(1000))
        result = merge_sort(original)
        self.assertEqual(result, original)
    
    def test_sort_large_reverse_list(self):
        """Trie une grande liste en ordre inverse."""
        original = list(range(1000, 0, -1))
        result = merge_sort(original)
        self.assertEqual(result, list(range(1, 1001)))
    
    def test_sort_very_large_list(self):
        """Trie une très grande liste."""
        import random
        original = [random.randint(-5000, 5000) for _ in range(1000)]
        result = merge_sort(original)
        
        # Vérifie que c'est trié
        for i in range(len(result) - 1):
            self.assertLessEqual(result[i], result[i + 1])


class TestMergeSortFloats(unittest.TestCase):
    """Tests avec des nombres à virgule."""
    
    def test_sort_floats(self):
        """Trie une liste de flottants."""
        result = merge_sort([3.5, 1.2, 4.8, 2.1, 5.9])
        self.assertEqual(result, [1.2, 2.1, 3.5, 4.8, 5.9])
    
    def test_sort_mixed_int_float(self):
        """Trie un mélange d'entiers et de flottants."""
        result = merge_sort([3, 1.5, 4, 2.5, 1])
        self.assertEqual(result, [1, 1.5, 2.5, 3, 4])


class TestMergeSortOddEvenLength(unittest.TestCase):
    """Tests avec des listes de longueur paire et impaire."""
    
    def test_sort_odd_length(self):
        """Trie une liste de longueur impaire."""
        result = merge_sort([5, 2, 8, 1, 9])
        self.assertEqual(result, [1, 2, 5, 8, 9])
    
    def test_sort_even_length(self):
        """Trie une liste de longueur paire."""
        result = merge_sort([5, 2, 8, 1])
        self.assertEqual(result, [1, 2, 5, 8])
    
    def test_sort_odd_length_large(self):
        """Trie une grande liste de longueur impaire."""
        result = merge_sort([7, 3, 9, 1, 5, 2, 8, 4, 6])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    def test_sort_even_length_large(self):
        """Trie une grande liste de longueur paire."""
        result = merge_sort([7, 3, 9, 1, 5, 2, 8, 4, 6, 10])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


class TestMergeSortReturnType(unittest.TestCase):
    """Tests du type de retour."""
    
    def test_returns_list(self):
        """Vérifie que la fonction retourne une liste."""
        result = merge_sort([3, 1, 2])
        self.assertIsInstance(result, list)
    
    def test_returns_new_list(self):
        """Vérifie que la fonction retourne une nouvelle liste."""
        original = [3, 1, 4, 2]
        result = merge_sort(original)
        
        # L'original ne doit pas être modifié
        self.assertEqual(original, [3, 1, 4, 2])
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_does_not_modify_original(self):
        """Vérifie que la liste originale n'est pas modifiée."""
        original = [5, 2, 8, 1, 9]
        original_copy = original.copy()
        merge_sort(original)
        
        self.assertEqual(original, original_copy)


class TestMergeSortCorrectness(unittest.TestCase):
    """Tests de vérification de la justesse."""
    
    def test_result_is_sorted(self):
        """Vérifie que le résultat est trié."""
        result = merge_sort([9, 3, 7, 1, 5, 2, 8, 4, 6])
        for i in range(len(result) - 1):
            self.assertLessEqual(result[i], result[i + 1])
    
    def test_all_elements_preserved(self):
        """Vérifie que tous les éléments sont préservés."""
        original = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = merge_sort(original)
        
        self.assertEqual(len(result), len(original))
        self.assertEqual(sorted(result), sorted(original))
    
    def test_no_extra_elements(self):
        """Vérifie qu'aucun élément supplémentaire n'est ajouté."""
        original = [7, 2, 9, 4, 1]
        result = merge_sort(original)
        
        self.assertEqual(sorted(result), sorted(original))
    
    def test_compare_with_python_sorted(self):
        """Compare avec la fonction sorted() de Python."""
        import random
        original = [random.randint(-100, 100) for _ in range(50)]
        result = merge_sort(original)
        expected = sorted(original)
        
        self.assertEqual(result, expected)


class TestMergeSortEdgeCases(unittest.TestCase):
    """Tests des cas limites."""
    
    def test_sort_alternating_high_low(self):
        """Trie une liste alternant hautes et basses valeurs."""
        result = merge_sort([10, 1, 9, 2, 8, 3, 7, 4, 6, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    def test_sort_peak_in_middle(self):
        """Trie une liste avec un pic au milieu."""
        result = merge_sort([1, 2, 3, 10, 4, 5, 6])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 10])
    
    def test_sort_valley_in_middle(self):
        """Trie une liste avec une vallée au milieu."""
        result = merge_sort([5, 4, 3, 1, 2, 6, 7])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7])
    
    def test_sort_power_of_two_length(self):
        """Trie une liste dont la longueur est une puissance de 2."""
        result = merge_sort([8, 4, 2, 1, 16, 32, 64, 128])
        self.assertEqual(result, [1, 2, 4, 8, 16, 32, 64, 128])
    
    def test_sort_non_power_of_two_length(self):
        """Trie une liste dont la longueur n'est pas une puissance de 2."""
        result = merge_sort([7, 5, 3, 1, 9, 11, 13])
        self.assertEqual(result, [1, 3, 5, 7, 9, 11, 13])


class TestMergeSortSpecialPatterns(unittest.TestCase):
    """Tests avec des motifs spéciaux."""
    
    def test_sort_two_groups(self):
        """Trie deux groupes distincts."""
        result = merge_sort([5, 6, 7, 8, 1, 2, 3, 4])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])
    
    def test_sort_fibonacci_sequence_unsorted(self):
        """Trie une séquence de Fibonacci non triée."""
        result = merge_sort([21, 1, 8, 3, 13, 5, 2, 1])
        self.assertEqual(result, [1, 1, 2, 3, 5, 8, 13, 21])
    
    def test_sort_squares(self):
        """Trie des nombres carrés."""
        result = merge_sort([16, 4, 1, 9, 25])
        self.assertEqual(result, [1, 4, 9, 16, 25])


if __name__ == '__main__':
    unittest.main(verbosity=2)
