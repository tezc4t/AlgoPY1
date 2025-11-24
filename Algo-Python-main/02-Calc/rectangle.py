"""
Module pour calculer l'aire d'un rectangle.
"""
# aire_rectangle L*l


# perimetre_rectangle 2*(L+l)



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
