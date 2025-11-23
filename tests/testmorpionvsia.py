import random

def afficher_plateau(plateau):
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 5)
 
def verifier_gagnant(plateau, joueur):
    # Vérifie les lignes
    for ligne in plateau:
        if all([case == joueur for case in ligne]):
            return True
    # Vérifie les colonnes
    for col in range(3):
        if all([plateau[row][col] == joueur for row in range(3)]):
            return True
    # Vérifie les diagonales
    if all([plateau[i][i] == joueur for i in range(3)]) or \
       all([plateau[i][2-i] == joueur for i in range(3)]):
       return True
    return False

def choisir_coup_machine(plateau):
    # IA simple : choisir une case libre au hasard
    cases_libres = []
    for l in range(3):
        for c in range(3):
            if plateau[l][c] == " ":
                cases_libres.append((l, c))
    return random.choice(cases_libres)

def jeu_morpion():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueur_actif = "X"
     
    for tour in range(9):
        afficher_plateau(plateau)

        if joueur_actif == "X":
            # Tour du joueur humain
            print(f"Joueur {joueur_actif}, à votre tour. Ecris le code de la colonne/ligne [(ligne du haut)(0,0) | (0,1) | (0,2)----ligne millieu---(1,0) | (1,1) | (1,2)---ligne bas---(2,0) | (2,1) | (2,2)]")

            while True:
                try:
                    l, c = map(int, input().split())
                    if 0 <= l < 3 and 0 <= c < 3 and plateau[l][c] == " ":
                        break
                    else:
                        print("Position non valide ou déjà occupée.")
                except ValueError:
                    print("Entrée invalide. Utilisez 'ligne colonne'.")
        else:
            # Tour de la machine
            print("Tour de la machine (O)...")
            l, c = choisir_coup_machine(plateau)

        # Placement sur le plateau
        plateau[l][c] = joueur_actif

        # Vérification victoire
        if verifier_gagnant(plateau, joueur_actif):
            afficher_plateau(plateau)
            print(f"Joueur {joueur_actif} gagne!")
            return

        # Changement de joueur
        joueur_actif = "O" if joueur_actif == "X" else "X"
     
    afficher_plateau(plateau)
    print("Match nul!")

jeu_morpion()
