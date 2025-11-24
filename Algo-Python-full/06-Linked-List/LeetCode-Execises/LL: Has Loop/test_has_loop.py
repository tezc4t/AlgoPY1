"""
Tests unitaires pour la méthode has_loop() de LinkedList.
Teste la détection de boucles dans une liste chaînée (Floyd's Cycle Detection).
"""

import unittest
from has_loop import Node, LinkedList


class TestHasLoop(unittest.TestCase):
    """Tests pour la méthode has_loop()."""
    
    def test_no_loop_single_node(self):
        """Liste avec un seul nœud, pas de boucle."""
        ll = LinkedList(1)
        
        result = ll.has_loop()
        
        self.assertFalse(result)
    
    def test_no_loop_multiple_nodes(self):
        """Liste avec plusieurs nœuds, pas de boucle."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        
        result = ll.has_loop()
        
        self.assertFalse(result)
    
    def test_loop_tail_to_head(self):
        """Boucle : le tail pointe vers le head."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        
        # Créer une boucle : tail -> head
        ll.tail.next = ll.head
        
        result = ll.has_loop()
        
        self.assertTrue(result)
    
    def test_loop_tail_to_middle(self):
        """Boucle : le tail pointe vers un nœud au milieu."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        
        # Récupérer le nœud au milieu (valeur 3)
        middle_node = ll.head.next.next
        
        # Créer une boucle : tail -> middle
        ll.tail.next = middle_node
        
        result = ll.has_loop()
        
        self.assertTrue(result)
    
    def test_loop_tail_to_itself(self):
        """Boucle : le tail pointe vers lui-même."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        
        # Créer une boucle : tail -> tail
        ll.tail.next = ll.tail
        
        result = ll.has_loop()
        
        self.assertTrue(result)
    
    def test_loop_second_node_to_first(self):
        """Boucle : le deuxième nœud pointe vers le premier."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        
        # Créer une boucle : nœud 2 -> nœud 1
        ll.head.next.next = ll.head
        
        result = ll.has_loop()
        
        self.assertTrue(result)
    
    def test_loop_in_middle(self):
        """Boucle au milieu de la liste."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        
        # Créer une boucle : nœud 4 -> nœud 2
        node2 = ll.head.next
        node4 = ll.head.next.next.next
        node4.next = node2
        
        result = ll.has_loop()
        
        self.assertTrue(result)
    
    def test_no_loop_two_nodes(self):
        """Liste avec deux nœuds, pas de boucle."""
        ll = LinkedList(1)
        ll.append(2)
        
        result = ll.has_loop()
        
        self.assertFalse(result)
    
    def test_loop_immediate_cycle(self):
        """Boucle immédiate : head pointe vers lui-même."""
        ll = LinkedList(1)
        
        # Créer une boucle : head -> head
        ll.head.next = ll.head
        
        result = ll.has_loop()
        
        self.assertTrue(result)
    
    def test_long_list_no_loop(self):
        """Longue liste sans boucle."""
        ll = LinkedList(1)
        for i in range(2, 101):
            ll.append(i)
        
        result = ll.has_loop()
        
        self.assertFalse(result)
    
    def test_long_list_with_loop(self):
        """Longue liste avec boucle."""
        ll = LinkedList(1)
        for i in range(2, 101):
            ll.append(i)
        
        # Créer une boucle du dernier au 50ème nœud
        node50 = ll.head
        for _ in range(49):
            node50 = node50.next
        
        ll.tail.next = node50
        
        result = ll.has_loop()
        
        self.assertTrue(result)


class TestHasLoopEdgeCases(unittest.TestCase):
    """Tests des cas limites pour has_loop()."""
    
    def test_empty_list_scenario(self):
        """
        Note : Notre implémentation ne permet pas de créer une liste vide
        directement, mais on peut tester avec head = None simulé.
        """
        ll = LinkedList(1)
        ll.head = None
        ll.tail = None
        ll.length = 0
        
        result = ll.has_loop()
        
        self.assertFalse(result)
    
    def test_list_after_creating_and_removing_loop(self):
        """Crée une boucle puis la supprime."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        
        # Créer une boucle
        ll.tail.next = ll.head
        self.assertTrue(ll.has_loop())
        
        # Supprimer la boucle
        ll.tail.next = None
        self.assertFalse(ll.has_loop())


class TestFloydAlgorithmProperties(unittest.TestCase):
    """Tests pour vérifier les propriétés de l'algorithme de Floyd."""
    
    def test_algorithm_efficiency(self):
        """
        Vérifie que l'algorithme fonctionne efficacement même avec
        une grande liste et une petite boucle.
        """
        ll = LinkedList(1)
        
        # Créer une liste de 1000 éléments
        for i in range(2, 1001):
            ll.append(i)
        
        # Créer une boucle sur les 5 derniers éléments
        node996 = ll.head
        for _ in range(995):
            node996 = node996.next
        
        ll.tail.next = node996
        
        result = ll.has_loop()
        
        self.assertTrue(result)
    
    def test_detect_loop_at_various_positions(self):
        """Détecte des boucles à différentes positions."""
        for loop_position in [1, 2, 3, 4, 5]:
            with self.subTest(loop_position=loop_position):
                ll = LinkedList(1)
                for i in range(2, 11):
                    ll.append(i)
                
                # Trouver le nœud à la position de boucle
                loop_node = ll.head
                for _ in range(loop_position - 1):
                    loop_node = loop_node.next
                
                # Créer la boucle
                ll.tail.next = loop_node
                
                self.assertTrue(ll.has_loop())


if __name__ == '__main__':
    unittest.main(verbosity=2)
