"""
Exercice 4 : Affichage itératif des nombres jusqu'à 500 avec while.
"""

def afficher_jusqu_a_500():
    nombre = 1
    
    while nombre <= 500:
        print(nombre)
        nombre += 1


def afficher_jusqu_a_limite(limite):
    nombre = 1
    
    while nombre <= limite:
        print(nombre)
        nombre += 1



if __name__ == "__main__":
    print("=== Affichage des nombres de 1 à 20 ===")
    afficher_jusqu_a_limite(20)
    

