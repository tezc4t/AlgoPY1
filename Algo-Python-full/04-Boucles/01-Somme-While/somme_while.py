"""
Exercice 1 : Calcul de la somme des nombres de 1 à 100 avec une boucle while.
"""

def somme_1_a_100():
    somme = 0
    nombre = 1
    
    while nombre <= 100:
        somme += nombre
        nombre += 1
    
    return somme


def somme_1_a_n(n):
    somme = 0
    nombre = 1
    
    while nombre <= n:
        somme += nombre
        nombre += 1
    
    return somme


if __name__ == "__main__":
    resultat = somme_1_a_100()
    print(f"La somme des nombres de 1 à 100 est : {resultat}")
    
    print("\nExemples avec d'autres valeurs :")
    for n in [5, 10, 50]:
        print(f"Somme de 1 à {n} = {somme_1_a_n(n)}")
