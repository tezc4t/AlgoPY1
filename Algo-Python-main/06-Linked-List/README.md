# Exercice : Implémentation d'une Liste Chaînée (Linked List)

## Objectif

Implémenter une structure de données de liste chaînée (Linked List) en Python avec ses opérations fondamentales.

## Description

Créez une classe `LinkedList` qui gère une liste chaînée. Cette structure utilise des nœuds (Node) liés entre eux par des pointeurs. Chaque nœud contient une valeur et une référence vers le nœud suivant.

## Structure de données

### Classe Node

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

### Classe LinkedList

```python
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
```

## Fonctions à implémenter

### 1. `append(value)`

Ajoute un élément à la fin de la liste.

- **Complexité :** O(1)
- **Retour :** `True`

### 2. `pop()`

Supprime et retourne le dernier élément de la liste.

- **Complexité :** O(n) - doit parcourir toute la liste
- **Retour :** Le nœud supprimé ou `None` si la liste est vide

### 3. `prepend(value)`

Ajoute un élément au début de la liste.

- **Complexité :** O(1)
- **Retour :** `True`

### 4. `pop_first()`

Supprime et retourne le premier élément de la liste.

- **Complexité :** O(1)
- **Retour :** Le nœud supprimé ou `None` si la liste est vide

### 5. `get(index)`

Retourne le nœud à l'index spécifié.

- **Complexité :** O(n)
- **Retour :** Le nœud à l'index ou `None` si l'index est invalide

### 6. `set_value(index, value)`

Modifie la valeur du nœud à l'index spécifié.

- **Complexité :** O(n)
- **Retour :** `True` si succès, `False` sinon

### 7. `insert(index, value)`

Insère un élément à l'index spécifié.

- **Complexité :** O(n)
- **Retour :** `True` si succès, `False` si l'index est invalide

### 8. `remove(index)`

Supprime l'élément à l'index spécifié.

- **Complexité :** O(n)
- **Retour :** Le nœud supprimé ou `None` si l'index est invalide

### 9. `reverse()`

Inverse l'ordre des éléments de la liste.

- **Complexité :** O(n)
- **Retour :** Aucun (modifie la liste en place)

### 10. `print_list()`

Affiche tous les éléments de la liste.

- **Complexité :** O(n)

## Utilisation

```python
# Créer une nouvelle liste chaînée
my_list = LinkedList(1)

# Ajouter des éléments
my_list.append(2)
my_list.append(3)
my_list.prepend(0)

# Afficher la liste
my_list.print_list()  # 0 -> 1 -> 2 -> 3

# Accéder à un élément
node = my_list.get(2)  # Récupère le nœud avec valeur 2

# Modifier un élément
my_list.set_value(1, 10)  # Change 1 en 10

# Insérer un élément
my_list.insert(2, 5)  # Insère 5 à l'index 2

# Supprimer un élément
removed = my_list.remove(1)  # Supprime l'élément à l'index 1

# Inverser la liste
my_list.reverse()
```

## Tests

Le fichier `test_list.py` contient des tests unitaires complets pour toutes les méthodes.

Pour exécuter les tests :

```bash
python test_list.py
```

Ou en mode verbose :

```bash
python -m unittest test_list.py -v
```

## Contraintes

- Gérer les cas limites (liste vide, index invalide, etc.)
- Maintenir à jour les pointeurs `head`, `tail` et `length`
- Retourner `None` en cas d'échec d'opération
- Les nœuds supprimés doivent avoir leur pointeur `next` mis à `None`

## Complexité Big O

| Opération | Complexité |
| --------- | ---------- |
| append    | O(1)       |
| pop       | O(n)       |
| prepend   | O(1)       |
| pop_first | O(1)       |
| get       | O(n)       |
| set_value | O(n)       |
| insert    | O(n)       |
| remove    | O(n)       |
| reverse   | O(n)       |

## Avantages de la Linked List

- Insertion/suppression en début de liste : O(1)
- Taille dynamique (pas besoin de réallouer la mémoire)
- Pas de gaspillage de mémoire

## Inconvénients

- Accès par index : O(n) au lieu de O(1)
- Plus de mémoire utilisée (stockage des pointeurs)
- Pas d'accès direct aux éléments

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
