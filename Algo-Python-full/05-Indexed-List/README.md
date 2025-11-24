# Exercice : Implémentation d'une Liste Indexée

## Objectif

Implémenter une structure de données de liste indexée (List) en Python avec ses opérations fondamentales.

## Description

Créez une classe `List` qui gère une liste indexée. Cette structure utilise un tableau dynamique pour stocker les éléments et permet un accès direct par index.

## Fonctions à implémenter

Vous devez implémenter les méthodes suivantes :

### 1. `append(value)`

Ajoute un élément à la fin de la liste.

### 2. `pop()`

Supprime et retourne le dernier élément de la liste.

### 3. `prepend(value)`

Ajoute un élément au début de la liste.

### 4. `pop_first()`

Supprime et retourne le premier élément de la liste.

### 5. `get(index)`

Retourne l'élément à l'index spécifié.

### 6. `set_value(index, value)`

Modifie la valeur de l'élément à l'index spécifié.

### 7. `insert(index, value)`

Insère un élément à l'index spécifié.

### 8. `remove(index)`

Supprime l'élément à l'index spécifié.

## Structure de départ

```python
class List:
    def __init__(self):
        self.items = []
```

## Contraintes

- Gérer les cas limites (liste vide, index invalide, etc.)
- Maintenir à jour la liste interne `items`
- Retourner `None` en cas d'échec d'opération
