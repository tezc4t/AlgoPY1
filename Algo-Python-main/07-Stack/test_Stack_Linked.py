"""
Tests unitaires pour l'implémentation de Stack (pile) avec liste chaînée.
Teste les opérations LIFO (Last In, First Out) de la pile.
"""

import unittest
from StackLinked import Node, StackLinked


class TestNode(unittest.TestCase):
    """Tests pour la classe Node."""
    
    def test_node_creation(self):
        """Vérifie la création d'un nœud."""
        node = Node(10)
        self.assertEqual(node.value, 10)
        self.assertIsNone(node.next)
    
    def test_node_with_string(self):
        """Vérifie la création d'un nœud avec une chaîne."""
        node = Node("data")
        self.assertEqual(node.value, "data")
        self.assertIsNone(node.next)


class TestStackInit(unittest.TestCase):
    """Tests pour l'initialisation de Stack."""
    
    def test_init_with_value(self):
        """Vérifie l'initialisation avec une valeur."""
        stack = StackLinked(5)
        self.assertEqual(stack.top.value, 5)
        self.assertEqual(stack.height, 1)
        self.assertIsNone(stack.top.next)
    
    def test_init_with_different_types(self):
        """Vérifie l'initialisation avec différents types."""
        stack_int = StackLinked(42)
        stack_str = StackLinked("hello")
        stack_float = StackLinked(3.14)
        
        self.assertEqual(stack_int.top.value, 42)
        self.assertEqual(stack_str.top.value, "hello")
        self.assertEqual(stack_float.top.value, 3.14)


class TestStackPush(unittest.TestCase):
    """Tests pour la méthode push()."""
    
    def test_push_to_stack(self):
        """Ajoute un élément à la pile."""
        stack = StackLinked(1)
        result = stack.push(2)
        
        self.assertTrue(result)
        self.assertEqual(stack.height, 2)
        self.assertEqual(stack.top.value, 2)
    
    def test_push_multiple_elements(self):
        """Ajoute plusieurs éléments."""
        stack = StackLinked(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        
        self.assertEqual(stack.height, 4)
        self.assertEqual(stack.top.value, 4)
    
    def test_push_maintains_lifo_order(self):
        """Vérifie que l'ordre LIFO est maintenu."""
        stack = StackLinked(1)
        stack.push(2)
        stack.push(3)
        
        # Le dernier ajouté (3) doit être au sommet
        self.assertEqual(stack.top.value, 3)
        self.assertEqual(stack.top.next.value, 2)
        self.assertEqual(stack.top.next.next.value, 1)
    
    def test_push_after_pop_all(self):
        """Ajoute après avoir vidé la pile."""
        stack = StackLinked(1)
        stack.pop()
        stack.push(10)
        
        self.assertEqual(stack.height, 1)
        self.assertEqual(stack.top.value, 10)
    
    def test_push_increments_height(self):
        """Vérifie que push incrémente height."""
        stack = StackLinked(1)
        initial_height = stack.height
        
        stack.push(2)
        
        self.assertEqual(stack.height, initial_height + 1)


class TestStackPop(unittest.TestCase):
    """Tests pour la méthode pop()."""
    
    def test_pop_from_stack(self):
        """Supprime un élément de la pile."""
        stack = StackLinked(1)
        stack.push(2)
        stack.push(3)
        
        popped = stack.pop()
        
        self.assertEqual(popped.value, 3)
        self.assertEqual(stack.height, 2)
        self.assertEqual(stack.top.value, 2)
    
    def test_pop_returns_top_element(self):
        """Vérifie que pop retourne le sommet."""
        stack = StackLinked(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        
        popped = stack.pop()
        
        self.assertEqual(popped.value, 4)
    
    def test_pop_single_element(self):
        """Supprime le seul élément de la pile."""
        stack = StackLinked(5)
        
        popped = stack.pop()
        
        self.assertEqual(popped.value, 5)
        self.assertEqual(stack.height, 0)
        self.assertIsNone(stack.top)
    
    def test_pop_empty_stack(self):
        """Pop sur une pile vide retourne None."""
        stack = StackLinked(1)
        stack.pop()
        
        result = stack.pop()
        
        self.assertIsNone(result)
        self.assertEqual(stack.height, 0)
    
    def test_pop_until_empty(self):
        """Supprime tous les éléments."""
        stack = StackLinked(1)
        stack.push(2)
        stack.push(3)
        
        popped1 = stack.pop()
        popped2 = stack.pop()
        popped3 = stack.pop()
        popped4 = stack.pop()
        
        self.assertEqual(popped1.value, 3)
        self.assertEqual(popped2.value, 2)
        self.assertEqual(popped3.value, 1)
        self.assertIsNone(popped4)
        self.assertEqual(stack.height, 0)
    
    def test_pop_decrements_height(self):
        """Vérifie que pop décrémente height."""
        stack = StackLinked(1)
        stack.push(2)
        initial_height = stack.height
        
        stack.pop()
        
        self.assertEqual(stack.height, initial_height - 1)
    
    def test_pop_disconnects_node(self):
        """Vérifie que le nœud supprimé est déconnecté."""
        stack = StackLinked(1)
        stack.push(2)
        
        popped = stack.pop()
        
        self.assertIsNone(popped.next)


class TestStackLIFO(unittest.TestCase):
    """Tests pour vérifier le comportement LIFO (Last In, First Out)."""
    
    def test_lifo_order(self):
        """Vérifie l'ordre LIFO strict."""
        stack = StackLinked(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        
        # Last In, First Out
        self.assertEqual(stack.pop().value, 4)
        self.assertEqual(stack.pop().value, 3)
        self.assertEqual(stack.pop().value, 2)
        self.assertEqual(stack.pop().value, 1)
    
    def test_push_pop_sequence(self):
        """Teste une séquence de push et pop."""
        stack = StackLinked(1)
        stack.push(2)
        stack.pop()  # Remove 2
        stack.push(3)
        stack.push(4)
        
        self.assertEqual(stack.pop().value, 4)
        self.assertEqual(stack.pop().value, 3)
        self.assertEqual(stack.pop().value, 1)
    
    def test_lifo_with_strings(self):
        """Vérifie LIFO avec des chaînes."""
        stack = StackLinked("first")
        stack.push("second")
        stack.push("third")
        
        self.assertEqual(stack.pop().value, "third")
        self.assertEqual(stack.pop().value, "second")
        self.assertEqual(stack.pop().value, "first")


class TestStackPrintStack(unittest.TestCase):
    """Tests pour la méthode print_stack()."""
    
    def test_print_stack_executes(self):
        """Vérifie que print_stack s'exécute sans erreur."""
        stack = StackLinked(1)
        stack.push(2)
        stack.push(3)
        
        try:
            stack.print_stack()
        except Exception as e:
            self.fail(f"print_stack() raised {e}")


if __name__ == '__main__':
    unittest.main(verbosity=2)
