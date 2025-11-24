def somme_matrice_3d(matrice):
    """
    Calcule la somme totale d'une matrice 3D.
    
    Args:
        matrice: Liste de listes de listes représentant une matrice 3D
        
    Returns:
        La somme de tous les éléments de la matrice
        
    Complexité: O(n × m × p) où n, m, p sont les dimensions
    """
    if not matrice:
        return 0
    
    somme = 0
    
    for plan in matrice:
        for ligne in plan:
            for valeur in ligne:
                somme += valeur
    
    return somme



# Exemples d'utilisation
if __name__ == "__main__":
  
    # Exercice 2: Somme d'une matrice 3D
    mat_3d = [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ]
    print("Exercice 2 - Somme matrice 3D:")
    print(f"Matrice: {mat_3d}")
    print(f"Somme totale: {somme_matrice_3d(mat_3d)} -> 36" )
    print(f"Complexité: O(n × m × p)\n")