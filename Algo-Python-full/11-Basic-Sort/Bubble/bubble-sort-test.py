import unittest
from bubble_sort import bubble_sort

"""
Tests unitaires pour la fonction bubble_sort.
"""



class TestBubbleSort(unittest.TestCase):
    """Classe de tests pour la fonction bubble_sort."""
    
    def test_bubble_sort_liste_desordonnee(self):
        """Test avec une liste désordonnée."""
        self.assertEqual(bubble_sort([4, 2, 6, 5, 1, 3]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(bubble_sort([9, 3, 7, 1, 5]), [1, 3, 5, 7, 9])
    
    def test_bubble_sort_liste_triee(self):
        """Test avec une liste déjà triée."""
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(bubble_sort([10, 20, 30]), [10, 20, 30])
    
    def test_bubble_sort_liste_inversee(self):
        """Test avec une liste triée en ordre inverse."""
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(bubble_sort([30, 20, 10]), [10, 20, 30])
    
    def test_bubble_sort_liste_vide(self):
        """Test avec une liste vide."""
        self.assertEqual(bubble_sort([]), [])
    
    def test_bubble_sort_un_element(self):
        """Test avec une liste à un seul élément."""
        self.assertEqual(bubble_sort([42]), [42])
        self.assertEqual(bubble_sort([0]), [0])
    
    def test_bubble_sort_deux_elements(self):
        """Test avec une liste à deux éléments."""
        self.assertEqual(bubble_sort([2, 1]), [1, 2])
        self.assertEqual(bubble_sort([1, 2]), [1, 2])
    
    def test_bubble_sort_doublons(self):
        """Test avec des valeurs en double."""
        self.assertEqual(bubble_sort([3, 1, 2, 1, 3]), [1, 1, 2, 3, 3])
        self.assertEqual(bubble_sort([5, 5, 5]), [5, 5, 5])
    
    def test_bubble_sort_nombres_negatifs(self):
        """Test avec des nombres négatifs."""
        self.assertEqual(bubble_sort([-1, -5, -3, -2]), [-5, -3, -2, -1])
        self.assertEqual(bubble_sort([3, -1, 0, -5, 2]), [-5, -1, 0, 2, 3])
    
    def test_bubble_sort_nombres_decimaux(self):
        """Test avec des nombres décimaux."""
        result = bubble_sort([3.5, 1.2, 2.8, 0.5])
        expected = [0.5, 1.2, 2.8, 3.5]
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i])
    
    def test_bubble_sort_grands_nombres(self):
        """Test avec de grands nombres."""
        self.assertEqual(bubble_sort([1000000, 500000, 2000000]), [500000, 1000000, 2000000])


if __name__ == '__main__':
    unittest.main()