
def max_matrice_2d(matrice):
    """
    Trouve la valeur maximale dans une matrice 2D.
    
    Args:
        matrice: Liste de listes représentant une matrice 2D
        
    Returns:
        La valeur maximale dans la matrice
        
    Complexité: O(n × m) où n = nombre de lignes, m = nombre de colonnes
    """
    if not matrice or not matrice[0]:
        return None
    
    max_val = matrice[0][0]
    
    for ligne in matrice:
        for valeur in ligne:
            if valeur > max_val:
                max_val = valeur
    
    return max_val

import unittest


    
    
    


class TestMaxMatrice2D(unittest.TestCase):
    """Tests pour la fonction max_matrice_2d()."""
    
    def test_max_matrice_simple(self):
        """Trouve le maximum dans une matrice simple."""
        matrice = [
            [3, 7, 2],
            [9, 1, 5],
            [4, 8, 6]
        ]
        self.assertEqual(max_matrice_2d(matrice), 9)
    
    def test_max_matrice_1x1(self):
        """Matrice avec un seul élément."""
        matrice = [[5]]
        self.assertEqual(max_matrice_2d(matrice), 5)
    
    def test_max_matrice_ligne(self):
        """Matrice d'une seule ligne."""
        matrice = [[1, 5, 3, 9, 2]]
        self.assertEqual(max_matrice_2d(matrice), 9)
    
    def test_max_matrice_colonne(self):
        """Matrice d'une seule colonne."""
        matrice = [[1], [5], [3], [9], [2]]
        self.assertEqual(max_matrice_2d(matrice), 9)
    
    def test_max_avec_negatifs(self):
        """Maximum dans une matrice avec valeurs négatives."""
        matrice = [
            [-5, -2, -8],
            [-1, -9, -3]
        ]
        self.assertEqual(max_matrice_2d(matrice), -1)
    
    def test_max_avec_zeros(self):
        """Maximum dans une matrice avec des zéros."""
        matrice = [
            [0, 0, 0],
            [0, 5, 0],
            [0, 0, 0]
        ]
        self.assertEqual(max_matrice_2d(matrice), 5)
    
    def test_max_tous_identiques(self):
        """Tous les éléments sont identiques."""
        matrice = [
            [7, 7, 7],
            [7, 7, 7]
        ]
        self.assertEqual(max_matrice_2d(matrice), 7)
    
    def test_max_matrice_vide(self):
        """Matrice vide."""
        matrice = []
        self.assertIsNone(max_matrice_2d(matrice))
    
    def test_max_matrice_avec_ligne_vide(self):
        """Matrice avec ligne vide."""
        matrice = [[]]
        self.assertIsNone(max_matrice_2d(matrice))
    
    def test_max_en_debut(self):
        """Maximum en position [0][0]."""
        matrice = [
            [100, 1, 2],
            [3, 4, 5]
        ]
        self.assertEqual(max_matrice_2d(matrice), 100)
    
    def test_max_en_fin(self):
        """Maximum en dernière position."""
        matrice = [
            [1, 2, 3],
            [4, 5, 100]
        ]
        self.assertEqual(max_matrice_2d(matrice), 100)


# Exemples d'utilisation
if __name__ == "__main__":
    # Exercice 1: Maximum dans une matrice 2D
    mat_2d = [
        [3, 7, 2],
        [9, 1, 5],
        [4, 8, 6]
    ]
    print("Exercice 1 - Maximum dans matrice 2D:")
    print(f"Matrice: {mat_2d}")
    print(f"Maximum: {max_matrice_2d(mat_2d)}")
    print(f"Complexité: O(n × m)\n")
    unittest.main(verbosity=2)