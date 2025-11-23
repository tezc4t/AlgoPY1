import turtle
import random

# Plateau
plateau = [[" " for _ in range(3)] for _ in range(3)]
joueur_actif = "X"

# Dessiner la grille
def dessiner_grille():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    for i in [-100, 0, 100]:
        # lignes horizontales
        turtle.goto(-150, i)
        turtle.pendown()
        turtle.forward(300)
        turtle.penup()
    turtle.left(90)
    for i in [-100, 0, 100]:
        # lignes verticales
        turtle.goto(i, 150)
        turtle.pendown()
        turtle.forward(300)
        turtle.penup()
    turtle.right(90)

# Dessiner X ou O
def dessiner_symbole(l, c, joueur):
    x = -150 + c*100 + 50
    y = 150 - l*100 - 50
    turtle.goto(x, y-25)
    turtle.write(joueur, align="center", font=("Arial", 36, "normal"))

# Vérification gagnant (utiliser ton code existant)
def verifier_gagnant(plateau, joueur):
    for ligne in plateau:
        if all([case == joueur for case in ligne]):
            return True
    for col in range(3):
        if all([plateau[row][col] == joueur for row in range(3)]):
            return True
    if all([plateau[i][i] == joueur for i in range(3)]) or \
       all([plateau[i][2-i] == joueur for i in range(3)]):
        return True
    return False

# IA simple
def choix_machine():
    cases_libres = [(l,c) for l in range(3) for c in range(3) if plateau[l][c]==" "]
    return random.choice(cases_libres)

# Gestion clic souris
def clic(x, y):
    global joueur_actif
    # Convertir coordonnées en l/c
    c = int((x + 150) // 100)
    l = int((150 - y) // 100)
    if plateau[l][c] != " ":
        return
    plateau[l][c] = joueur_actif
    dessiner_symbole(l, c, joueur_actif)
    if verifier_gagnant(plateau, joueur_actif):
        print(f"Joueur {joueur_actif} gagne !")
        turtle.done()
        return
    joueur_actif = "O" if joueur_actif=="X" else "X"

    # Si machine = O
    if joueur_actif == "O":
        l,c = choix_machine()
        plateau[l][c] = joueur_actif
        dessiner_symbole(l, c, joueur_actif)
        if verifier_gagnant(plateau, joueur_actif):
            print(f"Joueur {joueur_actif} gagne !")
            turtle.done()
            return
        joueur_actif = "X"

# Lancer le jeu
dessiner_grille()
turtle.onscreenclick(clic)
turtle.done()
