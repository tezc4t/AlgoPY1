"""
Tests unitaires pour l'implémentation de Queue (file) avec liste chaînée.
Teste les opérations FIFO (First In, First Out) de la file.
"""

import unittest
import sys
import importlib.util

# Importer le module avec un nom contenant un tiret
spec = importlib.util.spec_from_file_location(
    "queue_module",
    "/Users/francescohartemann/Documents/esiee/algo-python/08-Queue/QueueLinked.py"
)
queue_module = importlib.util.module_from_spec(spec)
sys.modules['queue_module'] = queue_module
spec.loader.exec_module(queue_module)

Queue = queue_module.Queue
Node = queue_module.Node


class TestQueueInit(unittest.TestCase):
    """Tests pour l'initialisation de Queue."""
    
    def test_init_creates_queue_with_one_node(self):
        """Vérifie l'initialisation avec une valeur."""
        queue = Queue(5)
        
        self.assertIsNotNone(queue.head)
        self.assertIsNotNone(queue.tail)
        self.assertEqual(queue.head.value, 5)
        self.assertEqual(queue.tail.value, 5)
        self.assertEqual(queue.length, 1)
    
    def test_init_head_and_tail_point_to_same_node(self):
        """Vérifie que head et tail pointent vers le même nœud."""
        queue = Queue(10)
        
        self.assertIs(queue.head, queue.tail)
    
    def test_init_node_next_is_none(self):
        """Vérifie que le nœud initial n'a pas de suivant."""
        queue = Queue(7)
        
        self.assertIsNone(queue.head.next)
    
    def test_init_with_different_types(self):
        """Vérifie l'initialisation avec différents types."""
        queue_int = Queue(42)
        queue_str = Queue("hello")
        queue_float = Queue(3.14)
        
        self.assertEqual(queue_int.head.value, 42)
        self.assertEqual(queue_str.head.value, "hello")
        self.assertEqual(queue_float.head.value, 3.14)


class TestQueueEnqueue(unittest.TestCase):
    """Tests pour la méthode enqueue()."""
    
    def test_enqueue_to_single_element_queue(self):
        """Ajoute un élément à une file avec un élément."""
        queue = Queue(1)
        result = queue.enqueue(2)
        
        self.assertTrue(result)
        self.assertEqual(queue.length, 2)
        self.assertEqual(queue.head.value, 1)
        self.assertEqual(queue.tail.value, 2)
    
    def test_enqueue_updates_tail(self):
        """Vérifie que enqueue met à jour tail."""
        queue = Queue(1)
        queue.enqueue(2)
        
        self.assertEqual(queue.tail.value, 2)
        self.assertIsNone(queue.tail.next)
    
    def test_enqueue_maintains_head(self):
        """Vérifie que enqueue ne change pas head."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        self.assertEqual(queue.head.value, 1)
    
    def test_enqueue_multiple_elements(self):
        """Ajoute plusieurs éléments."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        
        self.assertEqual(queue.length, 4)
        self.assertEqual(queue.head.value, 1)
        self.assertEqual(queue.tail.value, 4)
    
    def test_enqueue_creates_chain(self):
        """Vérifie que enqueue crée une chaîne correcte."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        self.assertEqual(queue.head.value, 1)
        self.assertEqual(queue.head.next.value, 2)
        self.assertEqual(queue.head.next.next.value, 3)
        self.assertIsNone(queue.head.next.next.next)
    
    def test_enqueue_increments_length(self):
        """Vérifie que enqueue incrémente length."""
        queue = Queue(1)
        initial_length = queue.length
        
        queue.enqueue(2)
        
        self.assertEqual(queue.length, initial_length + 1)
    
    def test_enqueue_returns_true(self):
        """Vérifie que enqueue retourne True."""
        queue = Queue(1)
        
        for i in range(5):
            result = queue.enqueue(i)
            self.assertTrue(result)


class TestQueueDequeue(unittest.TestCase):
    """Tests pour la méthode dequeue()."""
    
    def test_dequeue_from_queue_with_multiple_elements(self):
        """Supprime le premier élément d'une file."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        dequeued_node = queue.dequeue()
        
        self.assertEqual(dequeued_node.value, 1)
        self.assertEqual(queue.length, 2)
        self.assertEqual(queue.head.value, 2)
    
    def test_dequeue_returns_node(self):
        """Vérifie que dequeue retourne un nœud."""
        queue = Queue(5)
        queue.enqueue(10)
        
        result = queue.dequeue()
        
        self.assertIsInstance(result, Node)
        self.assertEqual(result.value, 5)
    
    def test_dequeue_returns_first_element(self):
        """Vérifie que dequeue retourne le premier élément (FIFO)."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        dequeued = queue.dequeue()
        
        self.assertEqual(dequeued.value, 1)
    
    def test_dequeue_empty_queue(self):
        """Dequeue sur une file vide retourne None."""
        queue = Queue(1)
        queue.dequeue()  # Remove the only element
        
        result = queue.dequeue()
        
        self.assertIsNone(result)
    
    def test_dequeue_single_element(self):
        """Supprime le seul élément de la file."""
        queue = Queue(5)
        
        dequeued = queue.dequeue()
        
        self.assertEqual(dequeued.value, 5)
        self.assertEqual(queue.length, 0)
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)
    
    def test_dequeue_until_empty(self):
        """Supprime tous les éléments."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        dequeued1 = queue.dequeue()
        dequeued2 = queue.dequeue()
        dequeued3 = queue.dequeue()
        dequeued4 = queue.dequeue()
        
        self.assertEqual(dequeued1.value, 1)
        self.assertEqual(dequeued2.value, 2)
        self.assertEqual(dequeued3.value, 3)
        self.assertIsNone(dequeued4)
        self.assertEqual(queue.length, 0)
    
    def test_dequeue_decrements_length(self):
        """Vérifie que dequeue décrémente length."""
        queue = Queue(1)
        queue.enqueue(2)
        
        initial_length = queue.length
        queue.dequeue()
        
        self.assertEqual(queue.length, initial_length - 1)
    
    def test_dequeue_updates_first(self):
        """Vérifie que dequeue met à jour head."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        queue.dequeue()
        
        self.assertEqual(queue.head.value, 2)
    
    def test_dequeue_isolates_node(self):
        """Vérifie que le nœud retourné est isolé."""
        queue = Queue(1)
        queue.enqueue(2)
        
        dequeued = queue.dequeue()
        
        self.assertIsNone(dequeued.next)


class TestQueueFIFO(unittest.TestCase):
    """Tests pour vérifier le comportement FIFO (First In, First Out)."""
    
    def test_fifo_order(self):
        """Vérifie l'ordre FIFO strict."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        
        # First In, First Out
        self.assertEqual(queue.dequeue().value, 1)
        self.assertEqual(queue.dequeue().value, 2)
        self.assertEqual(queue.dequeue().value, 3)
        self.assertEqual(queue.dequeue().value, 4)
    
    def test_enqueue_dequeue_sequence(self):
        """Teste une séquence d'enqueue et dequeue."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.dequeue()  # Remove 1
        queue.enqueue(3)
        queue.enqueue(4)
        
        self.assertEqual(queue.dequeue().value, 2)
        self.assertEqual(queue.dequeue().value, 3)
        self.assertEqual(queue.dequeue().value, 4)
    
    def test_fifo_with_strings(self):
        """Vérifie FIFO avec des chaînes."""
        queue = Queue("first")
        queue.enqueue("second")
        queue.enqueue("third")
        
        self.assertEqual(queue.dequeue().value, "first")
        self.assertEqual(queue.dequeue().value, "second")
        self.assertEqual(queue.dequeue().value, "third")
    
    def test_fifo_preserves_insertion_order(self):
        """Vérifie que l'ordre d'insertion est préservé."""
        queue = Queue(10)
        for i in range(20, 60, 10):
            queue.enqueue(i)
        
        self.assertEqual(queue.dequeue().value, 10)
        self.assertEqual(queue.dequeue().value, 20)
        self.assertEqual(queue.dequeue().value, 30)
        self.assertEqual(queue.dequeue().value, 40)
        self.assertEqual(queue.dequeue().value, 50)


class TestQueueLength(unittest.TestCase):
    """Tests pour l'attribut length."""
    
    def test_length_after_init(self):
        """Vérifie length après initialisation."""
        queue = Queue(1)
        self.assertEqual(queue.length, 1)
    
    def test_length_after_enqueues(self):
        """Vérifie length après plusieurs enqueues."""
        queue = Queue(1)
        
        for i in range(1, 6):
            queue.enqueue(i)
            self.assertEqual(queue.length, i + 1)
    
    def test_length_after_dequeues(self):
        """Vérifie length après plusieurs dequeues."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        
        self.assertEqual(queue.length, 4)
        
        queue.dequeue()
        self.assertEqual(queue.length, 3)
        
        queue.dequeue()
        self.assertEqual(queue.length, 2)
    
    def test_length_becomes_zero(self):
        """Vérifie que length devient 0."""
        queue = Queue(1)
        queue.dequeue()
        
        self.assertEqual(queue.length, 0)
    
    def test_length_accuracy_after_mixed_operations(self):
        """Vérifie l'exactitude de length après opérations mixtes."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.dequeue()
        queue.enqueue(4)
        queue.dequeue()
        
        self.assertEqual(queue.length, 2)


class TestQueueFirstLast(unittest.TestCase):
    """Tests pour les attributs head et tail."""
    
    def test_head_and_tail_after_enqueue(self):
        """Vérifie head et tail après enqueue."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        self.assertEqual(queue.head.value, 1)
        self.assertEqual(queue.tail.value, 3)
    
    def test_head_changes_after_dequeue(self):
        """Vérifie que head change après dequeue."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        queue.dequeue()
        
        self.assertEqual(queue.head.value, 2)
        self.assertEqual(queue.tail.value, 3)
    
    def test_head_and_tail_none_when_empty(self):
        """Vérifie que head et tail sont None quand la file est vide."""
        queue = Queue(1)
        queue.dequeue()
        
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)
    
    def test_head_and_tail_same_with_one_element(self):
        """Vérifie que head et tail pointent vers le même nœud avec un élément."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.dequeue()  # Now only one element (2) remains
        
        self.assertIs(queue.head, queue.tail)
        self.assertEqual(queue.head.value, 2)


class TestQueueIntegration(unittest.TestCase):
    """Tests d'intégration pour les opérations combinées."""
    
    def test_empty_and_rebuild(self):
        """Vide la file et la reconstruit."""
        queue = Queue(1)
        queue.enqueue(2)
        
        queue.dequeue()
        queue.dequeue()
        
        # File vide, mais on peut continuer à enqueue
        queue.enqueue(10)
        queue.enqueue(20)
        
        self.assertEqual(queue.length, 2)
        self.assertEqual(queue.head.value, 10)
        self.assertEqual(queue.tail.value, 20)
    
    def test_alternating_enqueue_dequeue(self):
        """Alterne entre enqueue et dequeue."""
        queue = Queue(1)
        
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue().value, 1)
        
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertEqual(queue.dequeue().value, 2)
        
        self.assertEqual(queue.length, 3)
        self.assertEqual(queue.head.value, 3)
    
    def test_large_queue(self):
        """Teste avec une grande file."""
        queue = Queue(0)
        
        # Ajouter 100 éléments
        for i in range(1, 101):
            queue.enqueue(i)
        
        self.assertEqual(queue.length, 101)
        self.assertEqual(queue.head.value, 0)
        self.assertEqual(queue.tail.value, 100)
        
        # Supprimer 50 éléments
        for i in range(50):
            dequeued = queue.dequeue()
            self.assertEqual(dequeued.value, i)
        
        self.assertEqual(queue.length, 51)
        self.assertEqual(queue.head.value, 50)
    
    def test_complex_operations(self):
        """Séquence complexe d'opérations."""
        queue = Queue(1)
        
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.head.value, 1)
        
        queue.dequeue()
        self.assertEqual(queue.head.value, 2)
        
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertEqual(queue.length, 4)
        
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(queue.head.value, 4)
        self.assertEqual(queue.tail.value, 5)


class TestQueueEdgeCases(unittest.TestCase):
    """Tests des cas limites."""
    
    def test_duplicate_values(self):
        """Teste avec des valeurs dupliquées."""
        queue = Queue(5)
        queue.enqueue(5)
        queue.enqueue(5)
        queue.enqueue(5)
        
        self.assertEqual(queue.length, 4)
        
        # Tous les dequeues doivent retourner 5
        for _ in range(4):
            self.assertEqual(queue.dequeue().value, 5)
    
    def test_zero_value(self):
        """Teste avec la valeur 0."""
        queue = Queue(0)
        
        self.assertEqual(queue.length, 1)
        self.assertEqual(queue.first.value, 0)
        self.assertEqual(queue.dequeue().value, 0)
    
    def test_negative_values(self):
        """Teste avec des valeurs négatives."""
        queue = Queue(-1)
        queue.enqueue(-2)
        queue.enqueue(-3)
        
        self.assertEqual(queue.dequeue().value, -1)
        self.assertEqual(queue.dequeue().value, -2)
        self.assertEqual(queue.dequeue().value, -3)
    
    def test_mixed_types(self):
        """Teste avec des types mixtes."""
        queue = Queue(1)
        queue.enqueue("two")
        queue.enqueue(3.0)
        queue.enqueue(True)
        
        self.assertEqual(queue.dequeue().value, 1)
        self.assertEqual(queue.dequeue().value, "two")
        self.assertEqual(queue.dequeue().value, 3.0)
        self.assertEqual(queue.dequeue().value, True)
    
    def test_none_value(self):
        """Teste avec None comme valeur."""
        queue = Queue(None)
        
        self.assertIsNone(queue.head.value)
        self.assertEqual(queue.length, 1)


class TestQueuePrintQueue(unittest.TestCase):
    """Tests pour la méthode print_queue()."""
    
    def test_print_queue_executes(self):
        """Vérifie que print_queue s'exécute sans erreur."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        try:
            queue.print_queue()
        except Exception as e:
            self.fail(f"print_queue() raised {e}")
    
    def test_print_single_element_queue(self):
        """Vérifie que print_queue fonctionne avec un élément."""
        queue = Queue(5)
        
        try:
            queue.print_queue()
        except Exception as e:
            self.fail(f"print_queue() on single element raised {e}")
    
    def test_print_after_dequeue(self):
        """Vérifie print_queue après dequeue."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.dequeue()
        
        try:
            queue.print_queue()
        except Exception as e:
            self.fail(f"print_queue() after dequeue raised {e}")


if __name__ == '__main__':
    unittest.main(verbosity=2)
