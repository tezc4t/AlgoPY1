"""
Exercice 2 : Affichage de fruits avec une boucle for.
"""

def afficher_fruits(fruits):
    for fruit in fruits:
        print(fruit)


def afficher_fruits_numerotes(fruits):
    for index, fruit in enumerate(fruits, start=1):
        print(f"{index}. {fruit}")


def obtenir_fruits_liste():
    return ["pomme", "banane", "orange", "fraise", "kiwi"]


if __name__ == "__main__":
    print("=== Affichage simple des fruits ===")
    fruits = obtenir_fruits_liste()
    afficher_fruits(fruits)
    
    print("\n=== Affichage numéroté des fruits ===")
    afficher_fruits_numerotes(fruits)
    
    print("\n=== Fruits personnalisés ===")
    mes_fruits = ["mangue", "ananas", "raisin", "melon", "cerise"]
    afficher_fruits(mes_fruits)
