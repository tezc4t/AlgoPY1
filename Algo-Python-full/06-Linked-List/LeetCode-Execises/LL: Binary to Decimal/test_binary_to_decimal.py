"""
Tests unitaires pour la méthode binary_to_decimal() de LinkedList.
Teste la conversion d'un nombre binaire stocké dans une liste chaînée en décimal.
"""

import unittest
from binary_to_decimal import Node, LinkedList


class TestBinaryToDecimal(unittest.TestCase):
    """Tests pour la méthode binary_to_decimal()."""
    
    def test_binary_0_equals_decimal_0(self):
        """Binaire 0 = Décimal 0."""
        ll = LinkedList(0)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 0)
    
    def test_binary_1_equals_decimal_1(self):
        """Binaire 1 = Décimal 1."""
        ll = LinkedList(1)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 1)
    
    def test_binary_10_equals_decimal_2(self):
        """Binaire 10 = Décimal 2."""
        ll = LinkedList(1)
        ll.append(0)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 2)
    
    def test_binary_11_equals_decimal_3(self):
        """Binaire 11 = Décimal 3."""
        ll = LinkedList(1)
        ll.append(1)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 3)
    
    def test_binary_100_equals_decimal_4(self):
        """Binaire 100 = Décimal 4."""
        ll = LinkedList(1)
        ll.append(0)
        ll.append(0)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 4)
    
    def test_binary_101_equals_decimal_5(self):
        """Binaire 101 = Décimal 5."""
        ll = LinkedList(1)
        ll.append(0)
        ll.append(1)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 5)
    
    def test_binary_110_equals_decimal_6(self):
        """Binaire 110 = Décimal 6."""
        ll = LinkedList(1)
        ll.append(1)
        ll.append(0)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 6)
    
    def test_binary_111_equals_decimal_7(self):
        """Binaire 111 = Décimal 7."""
        ll = LinkedList(1)
        ll.append(1)
        ll.append(1)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 7)
    
    def test_binary_1000_equals_decimal_8(self):
        """Binaire 1000 = Décimal 8."""
        ll = LinkedList(1)
        ll.append(0)
        ll.append(0)
        ll.append(0)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 8)
    
    def test_binary_1001_equals_decimal_9(self):
        """Binaire 1001 = Décimal 9."""
        ll = LinkedList(1)
        ll.append(0)
        ll.append(0)
        ll.append(1)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 9)
    
    def test_binary_1010_equals_decimal_10(self):
        """Binaire 1010 = Décimal 10."""
        ll = LinkedList(1)
        ll.append(0)
        ll.append(1)
        ll.append(0)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 10)
    
    def test_binary_1101_equals_decimal_13(self):
        """Binaire 1101 = Décimal 13."""
        ll = LinkedList(1)
        ll.append(1)
        ll.append(0)
        ll.append(1)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 13)
    
    def test_binary_1111_equals_decimal_15(self):
        """Binaire 1111 = Décimal 15."""
        ll = LinkedList(1)
        ll.append(1)
        ll.append(1)
        ll.append(1)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 15)
    
    def test_binary_10000_equals_decimal_16(self):
        """Binaire 10000 = Décimal 16."""
        ll = LinkedList(1)
        ll.append(0)
        ll.append(0)
        ll.append(0)
        ll.append(0)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 16)


class TestBinaryToDecimalLargeNumbers(unittest.TestCase):
    """Tests pour les grands nombres binaires."""
    
    def test_binary_11111111_equals_decimal_255(self):
        """Binaire 11111111 = Décimal 255 (8 bits)."""
        ll = LinkedList(1)
        for _ in range(7):
            ll.append(1)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 255)
    
    def test_binary_100000000_equals_decimal_256(self):
        """Binaire 100000000 = Décimal 256."""
        ll = LinkedList(1)
        for _ in range(8):
            ll.append(0)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 256)
    
    def test_binary_1111111111_equals_decimal_1023(self):
        """Binaire 1111111111 = Décimal 1023 (10 bits)."""
        ll = LinkedList(1)
        for _ in range(9):
            ll.append(1)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 1023)
    
    def test_binary_10000000000_equals_decimal_1024(self):
        """Binaire 10000000000 = Décimal 1024."""
        ll = LinkedList(1)
        for _ in range(10):
            ll.append(0)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 1024)


class TestBinaryToDecimalSpecialCases(unittest.TestCase):
    """Tests pour les cas spéciaux."""
    
    def test_all_zeros_except_first(self):
        """Nombre commençant par 1 suivi de zéros."""
        ll = LinkedList(1)
        ll.append(0)
        ll.append(0)
        ll.append(0)
        ll.append(0)
        ll.append(0)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 32)
    
    def test_alternating_bits(self):
        """Binaire 10101010 = Décimal 170."""
        ll = LinkedList(1)
        ll.append(0)
        ll.append(1)
        ll.append(0)
        ll.append(1)
        ll.append(0)
        ll.append(1)
        ll.append(0)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 170)
    
    def test_alternating_bits_reversed(self):
        """Binaire 01010101 = Décimal 85."""
        ll = LinkedList(0)
        ll.append(1)
        ll.append(0)
        ll.append(1)
        ll.append(0)
        ll.append(1)
        ll.append(0)
        ll.append(1)
        
        result = ll.binary_to_decimal()
        
        self.assertEqual(result, 85)


class TestBinaryToDecimalPowersOfTwo(unittest.TestCase):
    """Tests pour les puissances de 2."""
    
    def test_power_of_2_values(self):
        """Teste différentes puissances de 2."""
        test_cases = [
            (1, 1),      # 2^0 = 1
            (2, 2),      # 2^1 = 2
            (3, 4),      # 2^2 = 4
            (4, 8),      # 2^3 = 8
            (5, 16),     # 2^4 = 16
            (6, 32),     # 2^5 = 32
            (7, 64),     # 2^6 = 64
            (8, 128),    # 2^7 = 128
        ]
        
        for num_bits, expected_decimal in test_cases:
            with self.subTest(bits=num_bits, expected=expected_decimal):
                ll = LinkedList(1)
                for _ in range(num_bits - 1):
                    ll.append(0)
                
                result = ll.binary_to_decimal()
                
                self.assertEqual(result, expected_decimal)


class TestBinaryToDecimalAlgorithm(unittest.TestCase):
    """Tests pour vérifier les propriétés de l'algorithme."""
    
    def test_multiple_calls_same_result(self):
        """Appels multiples doivent retourner le même résultat."""
        ll = LinkedList(1)
        ll.append(0)
        ll.append(1)
        ll.append(1)
        
        result1 = ll.binary_to_decimal()
        result2 = ll.binary_to_decimal()
        result3 = ll.binary_to_decimal()
        
        self.assertEqual(result1, 11)
        self.assertEqual(result2, 11)
        self.assertEqual(result3, 11)
    
    def test_list_unchanged_after_conversion(self):
        """La liste ne doit pas être modifiée après conversion."""
        ll = LinkedList(1)
        ll.append(1)
        ll.append(0)
        
        # Sauvegarder les valeurs originales
        values_before = []
        temp = ll.head
        while temp:
            values_before.append(temp.value)
            temp = temp.next
        
        # Effectuer la conversion
        ll.binary_to_decimal()
        
        # Vérifier que les valeurs sont inchangées
        values_after = []
        temp = ll.head
        while temp:
            values_after.append(temp.value)
            temp = temp.next
        
        self.assertEqual(values_before, values_after)
    
    def test_known_conversions(self):
        """Teste plusieurs conversions connues."""
        test_data = [
            ([1, 0, 1, 0], 10),
            ([1, 1, 1, 1], 15),
            ([1, 0, 0, 0, 1], 17),
            ([1, 1, 0, 0, 1], 25),
            ([1, 0, 0, 1, 1], 19),
            ([1, 1, 1, 0, 0], 28),
        ]
        
        for binary_digits, expected_decimal in test_data:
            with self.subTest(binary=binary_digits, expected=expected_decimal):
                ll = LinkedList(binary_digits[0])
                for digit in binary_digits[1:]:
                    ll.append(digit)
                
                result = ll.binary_to_decimal()
                
                self.assertEqual(result, expected_decimal)


if __name__ == '__main__':
    unittest.main(verbosity=2)
