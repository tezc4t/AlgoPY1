
def coordonnees_minimum(matrice):
    """
    Trouve les coordonnées du minimum dans une matrice 2D.
    
    Args:
        matrice: Liste de listes représentant une matrice 2D
        
    Returns:
        Tuple (ligne, colonne) des coordonnées du minimum
        
    Complexité:
        - Au pire: O(n × m) - parcours complet
        - Au meilleur: O(1) - minimum en [0][0]
    """
    if not matrice or not matrice[0]:
        return None
    
    min_val = matrice[0][0]
    min_ligne = 0
    min_colonne = 0
    
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] < min_val:
                min_val = matrice[i][j]
                min_ligne = i
                min_colonne = j
    
    return (min_ligne, min_colonne)




import unittest

class TestCoordonneesMinimum(unittest.TestCase):
    """Tests pour la fonction coordonnees_minimum()."""
    
    def test_minimum_matrice_simple(self):
        """Trouve les coordonnées du minimum."""
        matrice = [
            [5, 3, 9],
            [7, 1, 6],
            [4, 8, 2]
        ]
        self.assertEqual(coordonnees_minimum(matrice), (1, 1))
    
    def test_minimum_en_debut(self):
        """Minimum en position [0][0]."""
        matrice = [
            [1, 5, 9],
            [7, 3, 6],
            [4, 8, 2]
        ]
        self.assertEqual(coordonnees_minimum(matrice), (0, 0))
    
    def test_minimum_en_fin(self):
        """Minimum en dernière position."""
        matrice = [
            [5, 3, 9],
            [7, 8, 6],
            [4, 2, 1]
        ]
        self.assertEqual(coordonnees_minimum(matrice), (2, 2))
    
    def test_minimum_matrice_1x1(self):
        """Matrice avec un seul élément."""
        matrice = [[42]]
        self.assertEqual(coordonnees_minimum(matrice), (0, 0))
    
    def test_minimum_ligne(self):
        """Matrice d'une seule ligne."""
        matrice = [[5, 2, 8, 1, 9]]
        self.assertEqual(coordonnees_minimum(matrice), (0, 3))
    
    def test_minimum_colonne(self):
        """Matrice d'une seule colonne."""
        matrice = [[5], [2], [8], [1], [9]]
        self.assertEqual(coordonnees_minimum(matrice), (3, 0))
    
    def test_minimum_avec_negatifs(self):
        """Minimum avec valeurs négatives."""
        matrice = [
            [5, -3, 9],
            [7, 1, -10],
            [4, 8, 2]
        ]
        self.assertEqual(coordonnees_minimum(matrice), (1, 2))
    
    def test_minimum_premier_occurrence(self):
        """Plusieurs minimums, retourne le premier trouvé."""
        matrice = [
            [5, 1, 9],
            [7, 3, 1],
            [4, 8, 2]
        ]
        # Premier 1 trouvé en (0, 1)
        self.assertEqual(coordonnees_minimum(matrice), (0, 1))
    
    def test_minimum_matrice_vide(self):
        """Matrice vide."""
        matrice = []
        self.assertIsNone(coordonnees_minimum(matrice))
    
    def test_minimum_ligne_vide(self):
        """Matrice avec ligne vide."""
        matrice = [[]]
        self.assertIsNone(coordonnees_minimum(matrice))
    
    def test_minimum_tous_identiques(self):
        """Tous les éléments sont identiques."""
        matrice = [
            [5, 5, 5],
            [5, 5, 5]
        ]
        self.assertEqual(coordonnees_minimum(matrice), (0, 0))



if __name__ == "__main__":
  
    # Exercice 3: Coordonnées du minimum
    mat_min = [
        [5, 3, 9],
        [7, 1, 6],
        [4, 8, 2]
    ]
    print("Exercice 3 - Coordonnées du minimum:")
    print(f"Matrice: {mat_min}")
    print(f"Coordonnées du minimum: {coordonnees_minimum(mat_min)}")
    print(f"Complexité: O(n × m) au pire, O(1) au meilleur\n")
    unittest.main(verbosity=2)