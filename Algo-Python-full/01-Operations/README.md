# Dossier Opérations

Ce dossier contient des fonctions d'opérations arithmétiques de base avec leurs tests unitaires.

## Contenu

- `addition.py` : Module contenant la fonction d'addition
- `test_addition.py` : Tests unitaires pour la fonction addition

## Fonction Addition

La fonction `addition(a, b)` permet d'additionner deux nombres (entiers ou décimaux).

### Utilisation

```python
from addition import addition

resultat = addition(5, 3)  # Retourne 8
```

## Exécution des tests

Pour exécuter les tests unitaires, utilisez la commande suivante dans le terminal :

```bash
python test_addition.py
```

Ou avec unittest en mode verbose :

```bash
python -m unittest test_addition.py -v
```

## Tests couverts

Les tests vérifient les cas suivants :

- Addition de nombres positifs
- Addition de nombres négatifs
- Addition mixte (positif + négatif)
- Addition avec zéro
- Addition de nombres décimaux
- Addition de grands nombres
