# Dossier Calc - Calculs géométriques

Ce dossier contient des fonctions pour effectuer des calculs géométriques sur des rectangles.

## Contenu

- `rectangle.py` : Module contenant les fonctions de calcul pour les rectangles
- `test_rectangle.py` : Tests unitaires pour les fonctions de rectangle

## Fonctions disponibles

### aire_rectangle(longueur, largeur)

Calcule l'aire d'un rectangle.

**Formule :** `aire = longueur × largeur`

```python
from rectangle import aire_rectangle

aire = aire_rectangle(10, 5)  # Retourne 50
```

### perimetre_rectangle(longueur, largeur)

Calcule le périmètre d'un rectangle.

**Formule :** `périmètre = 2 × (longueur + largeur)`

```python
from rectangle import perimetre_rectangle

perimetre = perimetre_rectangle(10, 5)  # Retourne 30
```

## Exécution du programme

Pour exécuter le programme avec un exemple :

```bash
python rectangle.py
```

## Exécution des tests

Pour exécuter les tests unitaires :

```bash
python test_rectangle.py
```

## Tests couverts

- Calculs avec nombres entiers
- Calculs avec nombres décimaux
- Cas avec zéro
- Grands nombres
- Petits nombres
- Cas particulier du carré
