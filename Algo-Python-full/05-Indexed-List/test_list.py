"""
Tests unitaires pour la classe IndexedList.
Chaque méthode possède sa propre classe de tests.
"""

import unittest
from list import IndexedList


class TestInit(unittest.TestCase):
    """Tests pour l'initialisation de IndexedList."""
    
    def test_init_avec_valeur(self):
        """Vérifie l'initialisation avec une valeur."""
        my_list = IndexedList(5)
        self.assertEqual(my_list.data, [5])
        self.assertEqual(my_list.length, 1)
    
    def test_init_avec_string(self):
        """Vérifie l'initialisation avec une chaîne."""
        my_list = IndexedList("hello")
        self.assertEqual(my_list.data, ["hello"])
        self.assertEqual(my_list.length, 1)


class TestAppend(unittest.TestCase):
    """Tests pour la méthode append()."""
    
    def test_append_un_element(self):
        """Ajoute un élément à la fin."""
        my_list = IndexedList(1)
        result = my_list.append(2)
        
        self.assertTrue(result)
        self.assertEqual(my_list.data, [1, 2])
        self.assertEqual(my_list.length, 2)
    
    def test_append_plusieurs_elements(self):
        """Ajoute plusieurs éléments."""
        my_list = IndexedList(1)
        my_list.append(2)
        my_list.append(3)
        my_list.append(4)
        
        self.assertEqual(my_list.data, [1, 2, 3, 4])
        self.assertEqual(my_list.length, 4)
    
    def test_append_types_differents(self):
        """Ajoute des éléments de types différents."""
        my_list = IndexedList(1)
        my_list.append("deux")
        my_list.append(3.5)
        
        self.assertEqual(my_list.data, [1, "deux", 3.5])
        self.assertEqual(my_list.length, 3)


# class TestPop(unittest.TestCase):
#     """Tests pour la méthode pop()."""
    
#     def test_pop_element(self):
#         """Supprime le dernier élément."""
#         my_list = IndexedList(1)
#         my_list.append(2)
#         my_list.append(3)
        
#         removed = my_list.pop()
        
#         self.assertEqual(removed, 3)
#         self.assertEqual(my_list.data, [1, 2])
#         self.assertEqual(my_list.length, 2)
    
#     def test_pop_jusqu_a_vide(self):
#         """Supprime tous les éléments."""
#         my_list = IndexedList(1)
        
#         removed1 = my_list.pop()
#         removed2 = my_list.pop()
        
#         self.assertEqual(removed1, 1)
#         self.assertIsNone(removed2)
#         self.assertEqual(my_list.data, [])
#         self.assertEqual(my_list.length, 0)
    
#     def test_pop_liste_vide(self):
#         """Pop sur une liste déjà vide."""
#         my_list = IndexedList(1)
#         my_list.pop()
        
#         result = my_list.pop()
        
#         self.assertIsNone(result)
#         self.assertEqual(my_list.length, 0)


# class TestPrepend(unittest.TestCase):
#     """Tests pour la méthode prepend()."""
    
#     def test_prepend_un_element(self):
#         """Ajoute un élément au début."""
#         my_list = IndexedList(2)
#         result = my_list.prepend(1)
        
#         self.assertTrue(result)
#         self.assertEqual(my_list.data, [1, 2])
#         self.assertEqual(my_list.length, 2)
    
#     def test_prepend_plusieurs_elements(self):
#         """Ajoute plusieurs éléments au début."""
#         my_list = IndexedList(3)
#         my_list.prepend(2)
#         my_list.prepend(1)
        
#         self.assertEqual(my_list.data, [1, 2, 3])
#         self.assertEqual(my_list.length, 3)


# class TestPopFirst(unittest.TestCase):
#     """Tests pour la méthode pop_first()."""
    
#     def test_pop_first_element(self):
#         """Supprime le premier élément."""
#         my_list = IndexedList(1)
#         my_list.append(2)
#         my_list.append(3)
        
#         removed = my_list.pop_first()
        
#         self.assertEqual(removed, 1)
#         self.assertEqual(my_list.data, [2, 3])
#         self.assertEqual(my_list.length, 2)
    
#     def test_pop_first_jusqu_a_vide(self):
#         """Supprime tous les éléments par le début."""
#         my_list = IndexedList(1)
#         my_list.append(2)
        
#         removed1 = my_list.pop_first()
#         removed2 = my_list.pop_first()
#         removed3 = my_list.pop_first()
        
#         self.assertEqual(removed1, 1)
#         self.assertEqual(removed2, 2)
#         self.assertIsNone(removed3)
#         self.assertEqual(my_list.length, 0)
    
#     def test_pop_first_liste_vide(self):
#         """Pop_first sur une liste vide."""
#         my_list = IndexedList(1)
#         my_list.pop()
        
#         result = my_list.pop_first()
        
#         self.assertIsNone(result)


# class TestGet(unittest.TestCase):
#     """Tests pour la méthode get()."""
    
#     def test_get_index_valide(self):
#         """Récupère un élément à un index valide."""
#         my_list = IndexedList(10)
#         my_list.append(20)
#         my_list.append(30)
        
#         self.assertEqual(my_list.get(0), 10)
#         self.assertEqual(my_list.get(1), 20)
#         self.assertEqual(my_list.get(2), 30)
    
#     def test_get_index_negatif(self):
#         """Récupère avec un index négatif."""
#         my_list = IndexedList(10)
        
#         result = my_list.get(-1)
        
#         self.assertIsNone(result)
    
#     def test_get_index_hors_limites(self):
#         """Récupère avec un index trop grand."""
#         my_list = IndexedList(10)
        
#         result = my_list.get(5)
        
#         self.assertIsNone(result)
    
#     def test_get_premier_et_dernier(self):
#         """Récupère le premier et dernier élément."""
#         my_list = IndexedList(1)
#         my_list.append(2)
#         my_list.append(3)
        
#         self.assertEqual(my_list.get(0), 1)
#         self.assertEqual(my_list.get(2), 3)


# class TestSetValue(unittest.TestCase):
#     """Tests pour la méthode set_value()."""
    
#     def test_set_value_index_valide(self):
#         """Modifie une valeur à un index valide."""
#         my_list = IndexedList(10)
#         my_list.append(20)
#         my_list.append(30)
        
#         result = my_list.set_value(1, 99)
        
#         self.assertTrue(result)
#         self.assertEqual(my_list.data, [10, 99, 30])
    
#     def test_set_value_premier_element(self):
#         """Modifie le premier élément."""
#         my_list = IndexedList(1)
        
#         result = my_list.set_value(0, 100)
        
#         self.assertTrue(result)
#         self.assertEqual(my_list.get(0), 100)
    
#     def test_set_value_index_negatif(self):
#         """Modifie avec un index négatif."""
#         my_list = IndexedList(10)
        
#         result = my_list.set_value(-1, 99)
        
#         self.assertFalse(result)
#         self.assertEqual(my_list.data, [10])
    
#     def test_set_value_index_hors_limites(self):
#         """Modifie avec un index trop grand."""
#         my_list = IndexedList(10)
        
#         result = my_list.set_value(5, 99)
        
#         self.assertFalse(result)
#         self.assertEqual(my_list.data, [10])


# class TestInsert(unittest.TestCase):
#     """Tests pour la méthode insert()."""
    
#     def test_insert_au_debut(self):
#         """Insère un élément au début."""
#         my_list = IndexedList(2)
#         my_list.append(3)
        
#         result = my_list.insert(0, 1)
        
#         self.assertTrue(result)
#         self.assertEqual(my_list.data, [1, 2, 3])
#         self.assertEqual(my_list.length, 3)
    
#     def test_insert_au_milieu(self):
#         """Insère un élément au milieu."""
#         my_list = IndexedList(1)
#         my_list.append(3)
        
#         result = my_list.insert(1, 2)
        
#         self.assertTrue(result)
#         self.assertEqual(my_list.data, [1, 2, 3])
#         self.assertEqual(my_list.length, 3)
    
#     def test_insert_a_la_fin(self):
#         """Insère un élément à la fin."""
#         my_list = IndexedList(1)
#         my_list.append(2)
        
#         result = my_list.insert(2, 3)
        
#         self.assertTrue(result)
#         self.assertEqual(my_list.data, [1, 2, 3])
#         self.assertEqual(my_list.length, 3)
    
#     def test_insert_index_negatif(self):
#         """Insère avec un index négatif."""
#         my_list = IndexedList(1)
        
#         result = my_list.insert(-1, 99)
        
#         self.assertFalse(result)
#         self.assertEqual(my_list.length, 1)
    
#     def test_insert_index_trop_grand(self):
#         """Insère avec un index trop grand."""
#         my_list = IndexedList(1)
        
#         result = my_list.insert(5, 99)
        
#         self.assertFalse(result)
#         self.assertEqual(my_list.length, 1)


# class TestRemove(unittest.TestCase):
#     """Tests pour la méthode remove()."""
    
#     def test_remove_au_debut(self):
#         """Supprime le premier élément."""
#         my_list = IndexedList(1)
#         my_list.append(2)
#         my_list.append(3)
        
#         removed = my_list.remove(0)
        
#         self.assertEqual(removed, 1)
#         self.assertEqual(my_list.data, [2, 3])
#         self.assertEqual(my_list.length, 2)
    
#     def test_remove_au_milieu(self):
#         """Supprime un élément au milieu."""
#         my_list = IndexedList(1)
#         my_list.append(2)
#         my_list.append(3)
        
#         removed = my_list.remove(1)
        
#         self.assertEqual(removed, 2)
#         self.assertEqual(my_list.data, [1, 3])
#         self.assertEqual(my_list.length, 2)
    
#     def test_remove_a_la_fin(self):
#         """Supprime le dernier élément."""
#         my_list = IndexedList(1)
#         my_list.append(2)
#         my_list.append(3)
        
#         removed = my_list.remove(2)
        
#         self.assertEqual(removed, 3)
#         self.assertEqual(my_list.data, [1, 2])
#         self.assertEqual(my_list.length, 2)
    
#     def test_remove_index_negatif(self):
#         """Supprime avec un index négatif."""
#         my_list = IndexedList(1)
        
#         result = my_list.remove(-1)
        
#         self.assertIsNone(result)
#         self.assertEqual(my_list.length, 1)
    
#     def test_remove_index_hors_limites(self):
#         """Supprime avec un index trop grand."""
#         my_list = IndexedList(1)
        
#         result = my_list.remove(5)
        
#         self.assertIsNone(result)
#         self.assertEqual(my_list.length, 1)
    
#     def test_remove_jusqu_a_vide(self):
#         """Supprime tous les éléments."""
#         my_list = IndexedList(1)
#         my_list.append(2)
        
#         my_list.remove(0)
#         my_list.remove(0)
        
#         self.assertEqual(my_list.data, [])
#         self.assertEqual(my_list.length, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
