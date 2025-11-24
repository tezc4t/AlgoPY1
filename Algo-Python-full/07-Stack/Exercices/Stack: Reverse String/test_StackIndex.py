"""
Tests unitaires pour l'implémentation de StackArray (pile avec tableau).
Teste les opérations LIFO (Last In, First Out) de la pile implémentée avec un tableau.
"""

import unittest
from StackIndex import StackArray


class TestStackArrayInit(unittest.TestCase):
    """Tests pour l'initialisation de StackArray."""
    
    def test_init_with_value(self):
        """Vérifie l'initialisation avec une valeur."""
        stack = StackArray(5)
        self.assertEqual(stack.stack, [5])
        self.assertEqual(stack.height(), 1)
    
    def test_init_without_value(self):
        """Vérifie l'initialisation sans valeur."""
        stack = StackArray()
        self.assertEqual(stack.stack, [])
        self.assertEqual(stack.height(), 0)
    
    def test_init_with_none(self):
        """Vérifie l'initialisation avec None explicite."""
        stack = StackArray(None)
        self.assertEqual(stack.stack, [])
        self.assertEqual(stack.height(), 0)
    
    def test_init_with_different_types(self):
        """Vérifie l'initialisation avec différents types."""
        stack_int = StackArray(42)
        stack_str = StackArray("hello")
        stack_float = StackArray(3.14)
        
        self.assertEqual(stack_int.stack[0], 42)
        self.assertEqual(stack_str.stack[0], "hello")
        self.assertEqual(stack_float.stack[0], 3.14)


class TestStackArrayPush(unittest.TestCase):
    """Tests pour la méthode push()."""
    
    def test_push_to_empty_stack(self):
        """Ajoute un élément à une pile vide."""
        stack = StackArray()
        result = stack.push(10)
        
        self.assertTrue(result)
        self.assertEqual(stack.height(), 1)
        self.assertEqual(stack.stack, [10])
    
    def test_push_to_non_empty_stack(self):
        """Ajoute un élément à une pile non vide."""
        stack = StackArray(1)
        result = stack.push(2)
        
        self.assertTrue(result)
        self.assertEqual(stack.height(), 2)
        self.assertEqual(stack.stack, [1, 2])
    
    def test_push_multiple_elements(self):
        """Ajoute plusieurs éléments."""
        stack = StackArray()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        
        self.assertEqual(stack.height(), 4)
        self.assertEqual(stack.stack, [1, 2, 3, 4])
    
    def test_push_maintains_order(self):
        """Vérifie que l'ordre d'ajout est maintenu."""
        stack = StackArray()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        
        self.assertEqual(stack.stack[0], 10)
        self.assertEqual(stack.stack[1], 20)
        self.assertEqual(stack.stack[2], 30)
    
    def test_push_always_returns_true(self):
        """Vérifie que push retourne toujours True."""
        stack = StackArray()
        
        for i in range(10):
            result = stack.push(i)
            self.assertTrue(result)


class TestStackArrayPop(unittest.TestCase):
    """Tests pour la méthode pop()."""
    
    def test_pop_from_stack(self):
        """Supprime un élément de la pile."""
        stack = StackArray()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        popped = stack.pop()
        
        self.assertEqual(popped, 3)
        self.assertEqual(stack.height(), 2)
        self.assertEqual(stack.stack, [1, 2])
    
    def test_pop_returns_last_element(self):
        """Vérifie que pop retourne le dernier élément (top)."""
        stack = StackArray()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        
        popped = stack.pop()
        
        self.assertEqual(popped, 30)
    
    def test_pop_empty_stack(self):
        """Pop sur une pile vide retourne None."""
        stack = StackArray()
        
        result = stack.pop()
        
        self.assertIsNone(result)
    
    def test_pop_single_element(self):
        """Supprime le seul élément de la pile."""
        stack = StackArray(5)
        
        popped = stack.pop()
        
        self.assertEqual(popped, 5)
        self.assertEqual(stack.height(), 0)
        self.assertEqual(stack.stack, [])
    
    def test_pop_until_empty(self):
        """Supprime tous les éléments."""
        stack = StackArray()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        popped1 = stack.pop()
        popped2 = stack.pop()
        popped3 = stack.pop()
        popped4 = stack.pop()
        
        self.assertEqual(popped1, 3)
        self.assertEqual(popped2, 2)
        self.assertEqual(popped3, 1)
        self.assertIsNone(popped4)
        self.assertEqual(stack.height(), 0)
    
    def test_pop_reduces_height(self):
        """Vérifie que pop réduit la hauteur."""
        stack = StackArray()
        stack.push(1)
        stack.push(2)
        
        initial_height = stack.height()
        stack.pop()
        
        self.assertEqual(stack.height(), initial_height - 1)


class TestStackArrayHeight(unittest.TestCase):
    """Tests pour la méthode height()."""
    
    def test_height_empty_stack(self):
        """Hauteur d'une pile vide."""
        stack = StackArray()
        self.assertEqual(stack.height(), 0)
    
    def test_height_single_element(self):
        """Hauteur avec un élément."""
        stack = StackArray(1)
        self.assertEqual(stack.height(), 1)
    
    def test_height_multiple_elements(self):
        """Hauteur avec plusieurs éléments."""
        stack = StackArray()
        
        for i in range(1, 11):
            stack.push(i)
            self.assertEqual(stack.height(), i)
    
    def test_height_after_operations(self):
        """Hauteur après plusieurs opérations."""
        stack = StackArray()
        
        self.assertEqual(stack.height(), 0)
        
        stack.push(1)
        self.assertEqual(stack.height(), 1)
        
        stack.push(2)
        self.assertEqual(stack.height(), 2)
        
        stack.pop()
        self.assertEqual(stack.height(), 1)
        
        stack.pop()
        self.assertEqual(stack.height(), 0)


class TestStackArrayTop(unittest.TestCase):
    """Tests pour la méthode top()."""
    
    def test_top_empty_stack(self):
        """Top d'une pile vide retourne None."""
        stack = StackArray()
        self.assertIsNone(stack.top())
    
    def test_top_single_element(self):
        """Top avec un seul élément."""
        stack = StackArray(42)
        self.assertEqual(stack.top(), 42)
    
    def test_top_multiple_elements(self):
        """Top retourne le dernier élément ajouté."""
        stack = StackArray()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        self.assertEqual(stack.top(), 3)
    
    def test_top_does_not_remove_element(self):
        """Vérifie que top ne supprime pas l'élément."""
        stack = StackArray()
        stack.push(1)
        stack.push(2)
        
        initial_height = stack.height()
        top_value = stack.top()
        
        self.assertEqual(top_value, 2)
        self.assertEqual(stack.height(), initial_height)
        self.assertEqual(stack.stack, [1, 2])
    
    def test_top_after_push(self):
        """Vérifie que top change après push."""
        stack = StackArray()
        stack.push(1)
        self.assertEqual(stack.top(), 1)
        
        stack.push(2)
        self.assertEqual(stack.top(), 2)
        
        stack.push(3)
        self.assertEqual(stack.top(), 3)
    
    def test_top_after_pop(self):
        """Vérifie que top change après pop."""
        stack = StackArray()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        self.assertEqual(stack.top(), 3)
        
        stack.pop()
        self.assertEqual(stack.top(), 2)
        
        stack.pop()
        self.assertEqual(stack.top(), 1)


class TestStackArrayLIFO(unittest.TestCase):
    """Tests pour vérifier le comportement LIFO (Last In, First Out)."""
    
    def test_lifo_order(self):
        """Vérifie l'ordre LIFO strict."""
        stack = StackArray()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        
        # Last In, First Out
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
    
    def test_push_pop_sequence(self):
        """Teste une séquence de push et pop."""
        stack = StackArray()
        stack.push(1)
        stack.push(2)
        stack.pop()  # Remove 2
        stack.push(3)
        stack.push(4)
        
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 1)
    
    def test_lifo_with_strings(self):
        """Vérifie LIFO avec des chaînes."""
        stack = StackArray()
        stack.push("first")
        stack.push("second")
        stack.push("third")
        
        self.assertEqual(stack.pop(), "third")
        self.assertEqual(stack.pop(), "second")
        self.assertEqual(stack.pop(), "first")


class TestStackArrayIntegration(unittest.TestCase):
    """Tests d'intégration pour les opérations combinées."""
    
    def test_empty_and_rebuild(self):
        """Vide la pile et la reconstruit."""
        stack = StackArray()
        stack.push(1)
        stack.push(2)
        
        stack.pop()
        stack.pop()
        
        stack.push(10)
        stack.push(20)
        
        self.assertEqual(stack.height(), 2)
        self.assertEqual(stack.top(), 20)
        self.assertEqual(stack.stack, [10, 20])
    
    def test_alternating_push_pop(self):
        """Alterne entre push et pop."""
        stack = StackArray()
        
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.pop(), 4)
        
        self.assertEqual(stack.height(), 2)
        self.assertEqual(stack.stack, [1, 3])
    
    def test_large_stack(self):
        """Teste avec une grande pile."""
        stack = StackArray()
        
        # Ajouter 100 éléments
        for i in range(1, 101):
            stack.push(i)
        
        self.assertEqual(stack.height(), 100)
        self.assertEqual(stack.top(), 100)
        
        # Supprimer 50 éléments
        for _ in range(50):
            stack.pop()
        
        self.assertEqual(stack.height(), 50)
        self.assertEqual(stack.top(), 50)
    
    def test_complex_operations(self):
        """Séquence complexe d'opérations."""
        stack = StackArray()
        
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.top(), 3)
        
        stack.pop()
        self.assertEqual(stack.top(), 2)
        
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.height(), 4)
        
        stack.pop()
        stack.pop()
        self.assertEqual(stack.stack, [1, 2])


class TestStackArrayEdgeCases(unittest.TestCase):
    """Tests des cas limites."""
    
    def test_duplicate_values(self):
        """Teste avec des valeurs dupliquées."""
        stack = StackArray()
        stack.push(5)
        stack.push(5)
        stack.push(5)
        stack.push(5)
        
        self.assertEqual(stack.height(), 4)
        
        # Tous les pops doivent retourner 5
        for _ in range(4):
            self.assertEqual(stack.pop(), 5)
    
    def test_zero_value(self):
        """Teste avec la valeur 0."""
        stack = StackArray(0)
        
        self.assertEqual(stack.height(), 1)
        self.assertEqual(stack.top(), 0)
        self.assertEqual(stack.pop(), 0)
    
    def test_negative_values(self):
        """Teste avec des valeurs négatives."""
        stack = StackArray()
        stack.push(-1)
        stack.push(-2)
        stack.push(-3)
        
        self.assertEqual(stack.pop(), -3)
        self.assertEqual(stack.pop(), -2)
        self.assertEqual(stack.pop(), -1)
    
    def test_mixed_types(self):
        """Teste avec des types mixtes."""
        stack = StackArray()
        stack.push(1)
        stack.push("two")
        stack.push(3.0)
        stack.push(True)
        
        self.assertEqual(stack.pop(), True)
        self.assertEqual(stack.pop(), 3.0)
        self.assertEqual(stack.pop(), "two")
        self.assertEqual(stack.pop(), 1)


class TestStackArrayPrintStack(unittest.TestCase):
    """Tests pour la méthode print_stack()."""
    
    def test_print_stack_executes(self):
        """Vérifie que print_stack s'exécute sans erreur."""
        stack = StackArray()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        try:
            stack.print_stack()
        except Exception as e:
            self.fail(f"print_stack() raised {e}")
    
    def test_print_empty_stack(self):
        """Vérifie que print_stack fonctionne sur une pile vide."""
        stack = StackArray()
        
        try:
            stack.print_stack()
        except Exception as e:
            self.fail(f"print_stack() on empty stack raised {e}")


if __name__ == '__main__':
    unittest.main(verbosity=2)
