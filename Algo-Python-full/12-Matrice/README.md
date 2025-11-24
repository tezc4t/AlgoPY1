# Exercices sur les Matrices

Ce dossier contient des exercices sur les opérations avec des matrices (tableaux à 2 et 3 dimensions).

## Exercices

### 1. Maximum dans une matrice 2D
Donné un tableau à 2 dimensions en entrée, écrire un algorithme qui permet de renvoyer la valeur maximale.

**Complexité:** O(n × m) où n est le nombre de lignes et m le nombre de colonnes.

### 2. Somme totale d'une matrice 3D
Donné un tableau à 3 dimensions en entrée, écrire un algorithme qui permet de renvoyer la somme totale.

**Complexité:** O(n × m × p) où n, m, p sont les dimensions du tableau 3D.

### 3. Coordonnées du minimum dans une matrice 2D
Donné un tableau à 2 dimensions, donner les coordonnées du minimum.

**Complexité:** 
- Au pire: O(n × m) - parcours complet de la matrice
- Au meilleur: O(1) - le minimum est en position [0][0]

### 4. Vérifier si une matrice est symétrique
Donné une matrice, vérifier si elle est symétrique, i.e. mat[i][j] = mat[j][i]

**Complexité:** O(n²) pour une matrice carrée n × n

## Fichiers

- `matrice.py` - Implémentation des fonctions
- `test_matrice.py` - Tests unitaires
