"""
Tests unitaires pour la méthode find_kth_from_end() de LinkedList.
Teste la recherche du k-ème nœud depuis la fin avec l'algorithme des deux pointeurs.
"""

import unittest
from find_kth_from_end import Node, LinkedList


class TestFindKthFromEnd(unittest.TestCase):
    """Tests pour la méthode find_kth_from_end()."""
    
    def test_find_last_node_k1(self):
        """k=1 retourne le dernier nœud."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        
        result = ll.find_kth_from_end(1)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 5)
    
    def test_find_second_from_end_k2(self):
        """k=2 retourne le deuxième nœud depuis la fin."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        
        result = ll.find_kth_from_end(2)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 4)
    
    def test_find_first_node_k_equals_length(self):
        """k=length retourne le premier nœud."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        
        result = ll.find_kth_from_end(5)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 1)
    
    def test_find_middle_node(self):
        """k au milieu de la liste."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        
        result = ll.find_kth_from_end(3)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 3)
    
    def test_k_greater_than_length(self):
        """k > length retourne None."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        
        result = ll.find_kth_from_end(5)
        
        self.assertIsNone(result)
    
    def test_k_zero(self):
        """k=0 retourne None ou le dernier élément selon implémentation."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        
        result = ll.find_kth_from_end(0)
        
        # k=0 devrait retourner None (hors limites)
        self.assertIsNone(result)
    
    def test_single_node_k1(self):
        """Liste avec un seul nœud, k=1."""
        ll = LinkedList(42)
        
        result = ll.find_kth_from_end(1)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 42)
    
    def test_single_node_k2(self):
        """Liste avec un seul nœud, k=2 retourne None."""
        ll = LinkedList(42)
        
        result = ll.find_kth_from_end(2)
        
        self.assertIsNone(result)
    
    def test_two_nodes_k1(self):
        """Deux nœuds, k=1 retourne le dernier."""
        ll = LinkedList(10)
        ll.append(20)
        
        result = ll.find_kth_from_end(1)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 20)
    
    def test_two_nodes_k2(self):
        """Deux nœuds, k=2 retourne le premier."""
        ll = LinkedList(10)
        ll.append(20)
        
        result = ll.find_kth_from_end(2)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 10)
    
    def test_long_list_k1(self):
        """Longue liste, k=1."""
        ll = LinkedList(1)
        for i in range(2, 101):
            ll.append(i)
        
        result = ll.find_kth_from_end(1)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 100)
    
    def test_long_list_k50(self):
        """Longue liste, k=50."""
        ll = LinkedList(1)
        for i in range(2, 101):
            ll.append(i)
        
        result = ll.find_kth_from_end(50)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 51)
    
    def test_long_list_k100(self):
        """Longue liste (100 éléments), k=100 retourne le premier."""
        ll = LinkedList(1)
        for i in range(2, 101):
            ll.append(i)
        
        result = ll.find_kth_from_end(100)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 1)
    
    def test_long_list_k101(self):
        """Longue liste (100 éléments), k=101 retourne None."""
        ll = LinkedList(1)
        for i in range(2, 101):
            ll.append(i)
        
        result = ll.find_kth_from_end(101)
        
        self.assertIsNone(result)


class TestFindKthFromEndEdgeCases(unittest.TestCase):
    """Tests des cas limites pour find_kth_from_end()."""
    
    def test_negative_k(self):
        """k négatif devrait retourner None."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        
        result = ll.find_kth_from_end(-1)
        
        # Selon l'implémentation, devrait retourner None
        self.assertIsNone(result)
    
    def test_all_positions_in_small_list(self):
        """Teste toutes les positions valides dans une petite liste."""
        ll = LinkedList(10)
        ll.append(20)
        ll.append(30)
        ll.append(40)
        ll.append(50)
        
        expected = {
            1: 50,
            2: 40,
            3: 30,
            4: 20,
            5: 10
        }
        
        for k, expected_value in expected.items():
            with self.subTest(k=k):
                result = ll.find_kth_from_end(k)
                self.assertIsNotNone(result)
                self.assertEqual(result.value, expected_value)
    
    def test_boundary_k_equals_length_plus_one(self):
        """k = length + 1 retourne None."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        
        result = ll.find_kth_from_end(4)
        
        self.assertIsNone(result)


class TestFindKthFromEndAlgorithm(unittest.TestCase):
    """Tests pour vérifier les propriétés de l'algorithme des deux pointeurs."""
    
    def test_string_values(self):
        """Teste avec des valeurs de type string."""
        ll = LinkedList("a")
        ll.append("b")
        ll.append("c")
        ll.append("d")
        ll.append("e")
        
        result = ll.find_kth_from_end(2)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.value, "d")
    
    def test_duplicate_values(self):
        """Teste avec des valeurs dupliquées."""
        ll = LinkedList(5)
        ll.append(5)
        ll.append(5)
        ll.append(5)
        
        # Devrait retourner le bon nœud même avec valeurs identiques
        result = ll.find_kth_from_end(3)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 5)
        # Vérifier que c'est bien le deuxième nœud (pas le premier)
        self.assertIs(result, ll.head.next)
    
    def test_returns_node_not_value(self):
        """Vérifie que la méthode retourne un nœud, pas une valeur."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        
        result = ll.find_kth_from_end(2)
        
        self.assertIsInstance(result, Node)
        self.assertTrue(hasattr(result, 'value'))
        self.assertTrue(hasattr(result, 'next'))
    
    def test_node_chain_integrity(self):
        """Vérifie que le nœud retourné fait partie de la chaîne."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        
        result = ll.find_kth_from_end(2)
        
        # Le nœud suivant devrait être le dernier
        self.assertEqual(result.next.value, 4)
        self.assertIsNone(result.next.next)
    
    def test_sequential_calls(self):
        """Appels séquentiels avec différentes valeurs de k."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        
        # Plusieurs appels ne doivent pas modifier la liste
        result1 = ll.find_kth_from_end(1)
        result2 = ll.find_kth_from_end(3)
        result3 = ll.find_kth_from_end(5)
        
        self.assertEqual(result1.value, 5)
        self.assertEqual(result2.value, 3)
        self.assertEqual(result3.value, 1)
        
        # La liste doit rester intacte
        self.assertEqual(ll.length, 5)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
