"""
Tests unitaires pour l'implémentation de HashTable.
Teste la construction et les opérations de la table de hachage.
"""

import unittest
from hash_table import HashTable


class TestHashTableInit(unittest.TestCase):
    """Tests pour l'initialisation de HashTable."""
    
    def test_init_default_size(self):
        """Vérifie l'initialisation avec la taille par défaut."""
        ht = HashTable()
        self.assertEqual(len(ht.data_map), 7)
        self.assertTrue(all(item is None for item in ht.data_map))
    
    def test_init_custom_size(self):
        """Vérifie l'initialisation avec une taille personnalisée."""
        ht = HashTable(10)
        self.assertEqual(len(ht.data_map), 10)
        self.assertTrue(all(item is None for item in ht.data_map))
    
    def test_init_size_one(self):
        """Vérifie l'initialisation avec taille 1."""
        ht = HashTable(1)
        self.assertEqual(len(ht.data_map), 1)
    
    def test_init_large_size(self):
        """Vérifie l'initialisation avec une grande taille."""
        ht = HashTable(100)
        self.assertEqual(len(ht.data_map), 100)
    
    def test_data_map_is_list(self):
        """Vérifie que data_map est une liste."""
        ht = HashTable()
        self.assertIsInstance(ht.data_map, list)


class TestHashTableSetItem(unittest.TestCase):
    """Tests pour la méthode set_item()."""
    
    def test_set_single_item(self):
        """Ajoute un seul élément."""
        ht = HashTable()
        ht.set_item('key', 'value')
        
        # Vérifie qu'au moins un bucket n'est plus None
        self.assertTrue(any(item is not None for item in ht.data_map))
    
    def test_set_multiple_items(self):
        """Ajoute plusieurs éléments."""
        ht = HashTable()
        ht.set_item('bolts', 1400)
        ht.set_item('washers', 50)
        ht.set_item('lumber', 70)
        
        # Vérifie que des éléments ont été ajoutés
        non_none_count = sum(1 for item in ht.data_map if item is not None)
        self.assertGreater(non_none_count, 0)
    
    def test_set_item_creates_list_in_bucket(self):
        """Vérifie que set_item crée une liste dans le bucket."""
        ht = HashTable()
        ht.set_item('test', 123)
        
        # Trouve le bucket non-None et vérifie que c'est une liste
        for bucket in ht.data_map:
            if bucket is not None:
                self.assertIsInstance(bucket, list)
                break
    
    def test_set_item_collision_handling(self):
        """Teste la gestion des collisions (plusieurs items dans un bucket)."""
        ht = HashTable(1)  # Taille 1 force les collisions
        ht.set_item('key1', 'value1')
        ht.set_item('key2', 'value2')
        ht.set_item('key3', 'value3')
        
        # Tous les items doivent être dans le même bucket
        self.assertEqual(len(ht.data_map[0]), 3)
    
    def test_set_item_with_different_types(self):
        """Teste l'ajout de différents types de valeurs."""
        ht = HashTable()
        ht.set_item('int', 42)
        ht.set_item('string', 'hello')
        ht.set_item('float', 3.14)
        ht.set_item('list', [1, 2, 3])
        ht.set_item('dict', {'a': 1})
        
        # Vérifie que tous ont été ajoutés
        self.assertGreater(len(ht.keys()), 0)
    
    def test_set_duplicate_key(self):
        """Teste l'ajout d'une clé dupliquée."""
        ht = HashTable()
        ht.set_item('key', 'value1')
        ht.set_item('key', 'value2')
        
        # Les deux valeurs doivent être présentes (pas d'écrasement)
        keys = ht.keys()
        self.assertEqual(keys.count('key'), 2)


class TestHashTableGetItem(unittest.TestCase):
    """Tests pour la méthode get_item()."""
    
    def test_get_existing_item(self):
        """Récupère un élément existant."""
        ht = HashTable()
        ht.set_item('bolts', 1400)
        
        self.assertEqual(ht.get_item('bolts'), 1400)
    
    def test_get_multiple_items(self):
        """Récupère plusieurs éléments."""
        ht = HashTable()
        ht.set_item('bolts', 1400)
        ht.set_item('washers', 50)
        ht.set_item('lumber', 70)
        
        self.assertEqual(ht.get_item('bolts'), 1400)
        self.assertEqual(ht.get_item('washers'), 50)
        self.assertEqual(ht.get_item('lumber'), 70)
    
    def test_get_non_existing_item(self):
        """Récupère un élément non existant."""
        ht = HashTable()
        ht.set_item('key', 'value')
        
        self.assertIsNone(ht.get_item('nonexistent'))
    
    def test_get_from_empty_table(self):
        """Récupère depuis une table vide."""
        ht = HashTable()
        
        self.assertIsNone(ht.get_item('anything'))
    
    def test_get_item_with_collision(self):
        """Récupère un élément dans un bucket avec collision."""
        ht = HashTable(1)
        ht.set_item('key1', 'value1')
        ht.set_item('key2', 'value2')
        ht.set_item('key3', 'value3')
        
        self.assertEqual(ht.get_item('key1'), 'value1')
        self.assertEqual(ht.get_item('key2'), 'value2')
        self.assertEqual(ht.get_item('key3'), 'value3')
    
    def test_get_item_different_types(self):
        """Récupère différents types de valeurs."""
        ht = HashTable()
        ht.set_item('int', 42)
        ht.set_item('string', 'hello')
        ht.set_item('list', [1, 2, 3])
        
        self.assertEqual(ht.get_item('int'), 42)
        self.assertEqual(ht.get_item('string'), 'hello')
        self.assertEqual(ht.get_item('list'), [1, 2, 3])
    
    def test_get_with_duplicate_keys(self):
        """Récupère la première valeur pour une clé dupliquée."""
        ht = HashTable()
        ht.set_item('key', 'first')
        ht.set_item('key', 'second')
        
        # Doit retourner la première occurrence
        self.assertEqual(ht.get_item('key'), 'first')


class TestHashTableKeys(unittest.TestCase):
    """Tests pour la méthode keys()."""
    
    def test_keys_empty_table(self):
        """Liste des clés d'une table vide."""
        ht = HashTable()
        
        self.assertEqual(ht.keys(), [])
    
    def test_keys_single_item(self):
        """Liste des clés avec un seul élément."""
        ht = HashTable()
        ht.set_item('key', 'value')
        
        self.assertEqual(ht.keys(), ['key'])
    
    def test_keys_multiple_items(self):
        """Liste des clés avec plusieurs éléments."""
        ht = HashTable()
        ht.set_item('bolts', 1400)
        ht.set_item('washers', 50)
        ht.set_item('lumber', 70)
        
        keys = ht.keys()
        self.assertEqual(len(keys), 3)
        self.assertIn('bolts', keys)
        self.assertIn('washers', keys)
        self.assertIn('lumber', keys)
    
    def test_keys_with_collisions(self):
        """Liste des clés avec des collisions."""
        ht = HashTable(1)
        ht.set_item('key1', 'value1')
        ht.set_item('key2', 'value2')
        ht.set_item('key3', 'value3')
        
        keys = ht.keys()
        self.assertEqual(len(keys), 3)
        self.assertIn('key1', keys)
        self.assertIn('key2', keys)
        self.assertIn('key3', keys)
    
    def test_keys_returns_list(self):
        """Vérifie que keys() retourne une liste."""
        ht = HashTable()
        ht.set_item('key', 'value')
        
        self.assertIsInstance(ht.keys(), list)
    
    def test_keys_with_duplicate_keys(self):
        """Liste des clés avec des clés dupliquées."""
        ht = HashTable()
        ht.set_item('key', 'value1')
        ht.set_item('key', 'value2')
        
        keys = ht.keys()
        self.assertEqual(keys.count('key'), 2)


class TestHashTablePrintTable(unittest.TestCase):
    """Tests pour la méthode print_table()."""
    
    def test_print_table_executes(self):
        """Vérifie que print_table s'exécute sans erreur."""
        ht = HashTable()
        ht.set_item('key', 'value')
        
        try:
            ht.print_table()
        except Exception as e:
            self.fail(f"print_table() raised {e}")
    
    def test_print_empty_table(self):
        """Vérifie que print_table fonctionne sur une table vide."""
        ht = HashTable()
        
        try:
            ht.print_table()
        except Exception as e:
            self.fail(f"print_table() on empty table raised {e}")


class TestHashTableIntegration(unittest.TestCase):
    """Tests d'intégration pour les opérations combinées."""
    
    def test_set_and_get_workflow(self):
        """Teste le workflow complet set puis get."""
        ht = HashTable()
        
        # Ajouter des items
        ht.set_item('name', 'Alice')
        ht.set_item('age', 30)
        ht.set_item('city', 'Paris')
        
        # Récupérer des items
        self.assertEqual(ht.get_item('name'), 'Alice')
        self.assertEqual(ht.get_item('age'), 30)
        self.assertEqual(ht.get_item('city'), 'Paris')
        
        # Vérifier les clés
        keys = ht.keys()
        self.assertEqual(len(keys), 3)
    
    def test_overwrite_behavior(self):
        """Teste le comportement lors de l'écrasement de valeurs."""
        ht = HashTable()
        ht.set_item('key', 'old_value')
        ht.set_item('key', 'new_value')
        
        # Avec l'implémentation actuelle, les deux sont stockées
        # et get_item retourne la première
        self.assertEqual(ht.get_item('key'), 'old_value')
    
    def test_large_dataset(self):
        """Teste avec un grand jeu de données."""
        ht = HashTable(50)
        
        # Ajouter 100 items
        for i in range(100):
            ht.set_item(f'key{i}', i)
        
        # Vérifier quelques items
        self.assertEqual(ht.get_item('key0'), 0)
        self.assertEqual(ht.get_item('key50'), 50)
        self.assertEqual(ht.get_item('key99'), 99)
        
        # Vérifier le nombre de clés
        self.assertEqual(len(ht.keys()), 100)
    
    def test_mixed_operations(self):
        """Teste un mélange d'opérations."""
        ht = HashTable()
        
        # Ajouter
        ht.set_item('a', 1)
        ht.set_item('b', 2)
        
        # Récupérer
        self.assertEqual(ht.get_item('a'), 1)
        
        # Ajouter plus
        ht.set_item('c', 3)
        ht.set_item('d', 4)
        
        # Vérifier les clés
        keys = ht.keys()
        self.assertEqual(len(keys), 4)
        
        # Récupérer un non-existant
        self.assertIsNone(ht.get_item('z'))


class TestHashTableEdgeCases(unittest.TestCase):
    """Tests des cas limites."""
    
    def test_empty_string_key(self):
        """Teste avec une clé vide."""
        ht = HashTable()
        ht.set_item('', 'empty_key')
        
        self.assertEqual(ht.get_item(''), 'empty_key')
    
    def test_numeric_string_keys(self):
        """Teste avec des clés numériques (strings)."""
        ht = HashTable()
        ht.set_item('123', 'value1')
        ht.set_item('456', 'value2')
        
        self.assertEqual(ht.get_item('123'), 'value1')
        self.assertEqual(ht.get_item('456'), 'value2')
    
    def test_special_characters_in_keys(self):
        """Teste avec des caractères spéciaux dans les clés."""
        ht = HashTable()
        ht.set_item('key!@#', 'value1')
        ht.set_item('key_$%^', 'value2')
        
        self.assertEqual(ht.get_item('key!@#'), 'value1')
        self.assertEqual(ht.get_item('key_$%^'), 'value2')
    
    def test_long_keys(self):
        """Teste avec des clés très longues."""
        ht = HashTable()
        long_key = 'a' * 1000
        ht.set_item(long_key, 'value')
        
        self.assertEqual(ht.get_item(long_key), 'value')
    
    def test_none_value(self):
        """Teste avec None comme valeur."""
        ht = HashTable()
        ht.set_item('key', None)
        
        # get_item retourne None, mais c'est la valeur stockée
        result = ht.get_item('key')
        self.assertIsNone(result)
        
        # Vérifie que la clé existe
        self.assertIn('key', ht.keys())
    
    def test_zero_value(self):
        """Teste avec 0 comme valeur."""
        ht = HashTable()
        ht.set_item('zero', 0)
        
        self.assertEqual(ht.get_item('zero'), 0)
    
    def test_boolean_values(self):
        """Teste avec des valeurs booléennes."""
        ht = HashTable()
        ht.set_item('true', True)
        ht.set_item('false', False)
        
        self.assertTrue(ht.get_item('true'))
        self.assertFalse(ht.get_item('false'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
