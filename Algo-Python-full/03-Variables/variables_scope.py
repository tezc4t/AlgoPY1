"""
Exercices sur les variables locales et globales en Python.
"""

# Exercice 1 : Variables Locales
def set_local():
    y = 15
    print(f"Variable locale y dans la fonction : {y}")


# Exercice 2 : Variables Globales
z = 30  # Variable globale


def modify_z():
    """
    Fonction qui modifie la variable globale z à 50.
    Utilise le mot-clé global pour modifier la variable globale.
    """
    global z
    z = 50
    print(f"Variable globale z modifiée dans la fonction : {z}")


if __name__ == "__main__":
    print("=== Exercice 1 : Variables Locales ===")
    print("\nAppel de set_local():")
    set_local()
    
    print("\nTentative d'accès à y en dehors de la fonction:")
    try:
        print(f"y = {y}")
    except NameError as e:
        print(f"Erreur : {e}")
        print("→ La variable y n'existe que dans la fonction set_local()")
        print("→ Elle n'est pas accessible en dehors de son scope local")
    
    print("\n" + "="*50)
    print("=== Exercice 2 : Variables Globales ===")
    print(f"\nVariable globale z avant modification : {z}")
    
    print("\nAppel de modify_z():")
    modify_z()
    
    print(f"\nVariable globale z après modification : {z}")


