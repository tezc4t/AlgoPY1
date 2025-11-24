"""
Module pour calculer l'aire d'un rectangle.
"""

def aire_rectangle(longueur, largeur):
    return longueur * largeur


def perimetre_rectangle(longueur, largeur):
    return 2 * (longueur + largeur)


if __name__ == "__main__":
    """
        __name__ est un variable python
     
        Pour que le même fichier puisse être :

        ✔ utilisé comme module
        ✔ ou exécuté comme programme principal
    """
    long = 10
    larg = 5
    
    print(f"Rectangle de {long} × {larg}")
    print(f"Aire : {aire_rectangle(long, larg)}")
    print(f"Périmètre : {perimetre_rectangle(long, larg)}")
