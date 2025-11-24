"""
Exercice 3 : Affichage des nombres de 1 à N avec une boucle for.
"""

def afficher_1_a_n(n):
    for nombre in range(1, n + 1):
        print(nombre)


def obtenir_liste_1_a_n(n):
    return [nombre for nombre in range(1, n + 1)]


def afficher_1_a_n_pairs_seulement(n):
    for nombre in range(1, n + 1):
        if nombre % 2 == 0:
            print(nombre)


if __name__ == "__main__":
    print("=== Nombres de 1 à 10 ===")
    afficher_1_a_n(10)
    
    print("\n=== Nombres pairs de 1 à 20 ===")
    afficher_1_a_n_pairs_seulement(20)
    
    print("\n=== Liste des nombres de 1 à 7 ===")
    liste = obtenir_liste_1_a_n(7)
    print(liste)
