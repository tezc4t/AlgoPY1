"""
Tests unitaires pour Binary Search Tree (BST).
Teste les opérations insert() et contains() sur un arbre binaire de recherche.
"""

import unittest
import sys

from bst_insert import BinarySearchTree, Node

class TestBSTInit(unittest.TestCase):
    """Tests pour l'initialisation de BinarySearchTree."""
    
    def test_init_empty_tree(self):
        """Vérifie l'initialisation d'un arbre vide."""
        tree = BinarySearchTree()
        self.assertIsNone(tree.root)
    
    def test_node_init(self):
        """Vérifie l'initialisation d'un nœud."""
        node = Node(10)
        self.assertEqual(node.value, 10)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)


class TestBSTInsert(unittest.TestCase):
    """Tests pour la méthode insert()."""
    
    def test_insert_first_node(self):
        """Insère le premier nœud (racine)."""
        tree = BinarySearchTree()
        result = tree.insert(10)
        
        self.assertTrue(result)
        self.assertIsNotNone(tree.root)
        self.assertEqual(tree.root.value, 10)
    
    def test_insert_left_child(self):
        """Insère un enfant gauche."""
        tree = BinarySearchTree()
        tree.insert(10)
        result = tree.insert(5)
        
        self.assertTrue(result)
        self.assertEqual(tree.root.left.value, 5)
    
    def test_insert_right_child(self):
        """Insère un enfant droit."""
        tree = BinarySearchTree()
        tree.insert(10)
        result = tree.insert(15)
        
        self.assertTrue(result)
        self.assertEqual(tree.root.right.value, 15)
    
    def test_insert_multiple_nodes(self):
        """Insère plusieurs nœuds."""
        tree = BinarySearchTree()
        tree.insert(47)
        tree.insert(21)
        tree.insert(76)
        tree.insert(18)
        tree.insert(27)
        tree.insert(52)
        tree.insert(82)
        
        self.assertEqual(tree.root.value, 47)
        self.assertEqual(tree.root.left.value, 21)
        self.assertEqual(tree.root.right.value, 76)
        self.assertEqual(tree.root.left.left.value, 18)
        self.assertEqual(tree.root.left.right.value, 27)
        self.assertEqual(tree.root.right.left.value, 52)
        self.assertEqual(tree.root.right.right.value, 82)
    
    def test_insert_duplicate_returns_false(self):
        """Insère une valeur dupliquée retourne False."""
        tree = BinarySearchTree()
        tree.insert(10)
        result = tree.insert(10)
        
        self.assertFalse(result)
    
    def test_insert_ascending_order(self):
        """Insère en ordre ascendant."""
        tree = BinarySearchTree()
        tree.insert(1)
        tree.insert(2)
        tree.insert(3)
        tree.insert(4)
        tree.insert(5)
        
        # Tous à droite (arbre déséquilibré)
        self.assertEqual(tree.root.value, 1)
        self.assertEqual(tree.root.right.value, 2)
        self.assertEqual(tree.root.right.right.value, 3)
    
    def test_insert_descending_order(self):
        """Insère en ordre descendant."""
        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(4)
        tree.insert(3)
        tree.insert(2)
        tree.insert(1)
        
        # Tous à gauche (arbre déséquilibré)
        self.assertEqual(tree.root.value, 5)
        self.assertEqual(tree.root.left.value, 4)
        self.assertEqual(tree.root.left.left.value, 3)
    
    def test_insert_returns_true_on_success(self):
        """Vérifie que insert retourne True en cas de succès."""
        tree = BinarySearchTree()
        
        for i in [10, 5, 15, 3, 7, 12, 20]:
            result = tree.insert(i)
            self.assertTrue(result)


class TestBSTContains(unittest.TestCase):
    """Tests pour la méthode contains()."""
    
    def test_contains_in_tree(self):
        """Vérifie qu'un élément est dans l'arbre."""
        tree = BinarySearchTree()
        tree.insert(47)
        tree.insert(21)
        tree.insert(76)
        tree.insert(18)
        tree.insert(27)
        tree.insert(52)
        tree.insert(82)
        
        self.assertTrue(tree.contains(27))
    
    def test_contains_not_in_tree(self):
        """Vérifie qu'un élément n'est pas dans l'arbre."""
        tree = BinarySearchTree()
        tree.insert(47)
        tree.insert(21)
        tree.insert(76)
        tree.insert(18)
        tree.insert(27)
        tree.insert(52)
        tree.insert(82)
        
        self.assertFalse(tree.contains(17))
    
    def test_contains_root_value(self):
        """Vérifie la présence de la racine."""
        tree = BinarySearchTree()
        tree.insert(10)
        
        self.assertTrue(tree.contains(10))
    
    def test_contains_left_child(self):
        """Vérifie la présence d'un enfant gauche."""
        tree = BinarySearchTree()
        tree.insert(10)
        tree.insert(5)
        
        self.assertTrue(tree.contains(5))
    
    def test_contains_right_child(self):
        """Vérifie la présence d'un enfant droit."""
        tree = BinarySearchTree()
        tree.insert(10)
        tree.insert(15)
        
        self.assertTrue(tree.contains(15))
    
    def test_contains_empty_tree(self):
        """Vérifie dans un arbre vide."""
        tree = BinarySearchTree()
        
        self.assertFalse(tree.contains(10))
    
    def test_contains_all_inserted_values(self):
        """Vérifie que toutes les valeurs insérées sont trouvées."""
        tree = BinarySearchTree()
        values = [47, 21, 76, 18, 27, 52, 82]
        
        for value in values:
            tree.insert(value)
        
        for value in values:
            self.assertTrue(tree.contains(value))
    
    def test_contains_none_of_missing_values(self):
        """Vérifie qu'aucune valeur manquante n'est trouvée."""
        tree = BinarySearchTree()
        tree.insert(47)
        tree.insert(21)
        tree.insert(76)
        
        missing_values = [10, 30, 50, 100]
        for value in missing_values:
            self.assertFalse(tree.contains(value))


class TestBSTInsertAndContains(unittest.TestCase):
    """Tests d'intégration pour insert et contains."""
    
    def test_insert_and_find(self):
        """Insère et trouve des éléments."""
        tree = BinarySearchTree()
        
        tree.insert(50)
        self.assertTrue(tree.contains(50))
        
        tree.insert(25)
        self.assertTrue(tree.contains(25))
        
        tree.insert(75)
        self.assertTrue(tree.contains(75))
    
    def test_insert_many_find_all(self):
        """Insère beaucoup d'éléments et les trouve tous."""
        tree = BinarySearchTree()
        values = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43]
        
        for value in values:
            tree.insert(value)
        
        for value in values:
            self.assertTrue(tree.contains(value))
    
    def test_duplicate_not_found_twice(self):
        """Vérifie qu'un doublon n'est pas trouvé deux fois."""
        tree = BinarySearchTree()
        tree.insert(10)
        tree.insert(10)  # Devrait retourner False
        
        # Mais 10 devrait toujours être trouvé
        self.assertTrue(tree.contains(10))


class TestBSTWithNegativeNumbers(unittest.TestCase):
    """Tests avec des nombres négatifs."""
    
    def test_insert_negative_numbers(self):
        """Insère des nombres négatifs."""
        tree = BinarySearchTree()
        tree.insert(0)
        tree.insert(-5)
        tree.insert(5)
        tree.insert(-10)
        tree.insert(-2)
        
        self.assertTrue(tree.contains(-5))
        self.assertTrue(tree.contains(-10))
        self.assertTrue(tree.contains(-2))
    
    def test_contains_negative_numbers(self):
        """Vérifie la présence de nombres négatifs."""
        tree = BinarySearchTree()
        tree.insert(-10)
        tree.insert(-20)
        tree.insert(-5)
        
        self.assertTrue(tree.contains(-20))
        self.assertFalse(tree.contains(-15))


class TestBSTWithZero(unittest.TestCase):
    """Tests avec la valeur zéro."""
    
    def test_insert_zero(self):
        """Insère zéro."""
        tree = BinarySearchTree()
        result = tree.insert(0)
        
        self.assertTrue(result)
        self.assertEqual(tree.root.value, 0)
    
    def test_contains_zero(self):
        """Vérifie la présence de zéro."""
        tree = BinarySearchTree()
        tree.insert(10)
        tree.insert(0)
        tree.insert(20)
        
        self.assertTrue(tree.contains(0))
    
    def test_tree_with_zero_as_root(self):
        """Arbre avec zéro comme racine."""
        tree = BinarySearchTree()
        tree.insert(0)
        tree.insert(-5)
        tree.insert(5)
        
        self.assertTrue(tree.contains(0))
        self.assertTrue(tree.contains(-5))
        self.assertTrue(tree.contains(5))


class TestBSTEdgeCases(unittest.TestCase):
    """Tests des cas limites."""
    
    def test_single_node_tree(self):
        """Arbre avec un seul nœud."""
        tree = BinarySearchTree()
        tree.insert(42)
        
        self.assertTrue(tree.contains(42))
        self.assertFalse(tree.contains(41))
        self.assertFalse(tree.contains(43))
    
    def test_left_only_tree(self):
        """Arbre uniquement à gauche."""
        tree = BinarySearchTree()
        tree.insert(10)
        tree.insert(9)
        tree.insert(8)
        tree.insert(7)
        
        self.assertTrue(tree.contains(7))
        self.assertTrue(tree.contains(8))
        self.assertTrue(tree.contains(9))
        self.assertTrue(tree.contains(10))
    
    def test_right_only_tree(self):
        """Arbre uniquement à droite."""
        tree = BinarySearchTree()
        tree.insert(10)
        tree.insert(11)
        tree.insert(12)
        tree.insert(13)
        
        self.assertTrue(tree.contains(10))
        self.assertTrue(tree.contains(11))
        self.assertTrue(tree.contains(12))
        self.assertTrue(tree.contains(13))
    
    def test_balanced_tree(self):
        """Arbre équilibré."""
        tree = BinarySearchTree()
        tree.insert(50)
        tree.insert(25)
        tree.insert(75)
        tree.insert(12)
        tree.insert(37)
        tree.insert(62)
        tree.insert(87)
        
        for value in [50, 25, 75, 12, 37, 62, 87]:
            self.assertTrue(tree.contains(value))


class TestBSTLargeDataset(unittest.TestCase):
    """Tests avec de grands ensembles de données."""
    
    def test_insert_many_values(self):
        """Insère beaucoup de valeurs."""
        tree = BinarySearchTree()
        
        for i in range(100):
            tree.insert(i)
        
        # Vérifie quelques valeurs
        self.assertTrue(tree.contains(0))
        self.assertTrue(tree.contains(50))
        self.assertTrue(tree.contains(99))
        self.assertFalse(tree.contains(100))
    
    def test_insert_and_find_random_values(self):
        """Insère et trouve des valeurs aléatoires."""
        import random
        tree = BinarySearchTree()
        values = random.sample(range(1000), 100)
        
        for value in values:
            tree.insert(value)
        
        for value in values:
            self.assertTrue(tree.contains(value))


class TestBSTReturnValues(unittest.TestCase):
    """Tests des valeurs de retour."""
    
    def test_insert_returns_boolean(self):
        """Vérifie que insert retourne un booléen."""
        tree = BinarySearchTree()
        result = tree.insert(10)
        
        self.assertIsInstance(result, bool)
    
    def test_contains_returns_boolean(self):
        """Vérifie que contains retourne un booléen."""
        tree = BinarySearchTree()
        tree.insert(10)
        
        result_true = tree.contains(10)
        result_false = tree.contains(20)
        
        self.assertIsInstance(result_true, bool)
        self.assertIsInstance(result_false, bool)


class TestBSTStructure(unittest.TestCase):
    """Tests de la structure de l'arbre."""
    
    def test_left_subtree_smaller(self):
        """Vérifie que le sous-arbre gauche contient des valeurs plus petites."""
        tree = BinarySearchTree()
        tree.insert(50)
        tree.insert(25)
        tree.insert(75)
        tree.insert(12)
        tree.insert(37)
        
        # Tous les nœuds à gauche de 50 doivent être < 50
        self.assertLess(tree.root.left.value, tree.root.value)
        self.assertLess(tree.root.left.left.value, tree.root.value)
        self.assertLess(tree.root.left.right.value, tree.root.value)
    
    def test_right_subtree_larger(self):
        """Vérifie que le sous-arbre droit contient des valeurs plus grandes."""
        tree = BinarySearchTree()
        tree.insert(50)
        tree.insert(25)
        tree.insert(75)
        tree.insert(62)
        tree.insert(87)
        
        # Tous les nœuds à droite de 50 doivent être > 50
        self.assertGreater(tree.root.right.value, tree.root.value)
        self.assertGreater(tree.root.right.left.value, tree.root.value)
        self.assertGreater(tree.root.right.right.value, tree.root.value)


if __name__ == '__main__':
    unittest.main(verbosity=2)
