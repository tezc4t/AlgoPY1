# Exercices sur les Variables Locales et Globales

Ce dossier contient des exercices pour comprendre la portée (scope) des variables en Python.

## Contenu

- `variables_scope.py` : Fichier principal avec les exercices
- `test_variables_scope.py` : Tests unitaires

## Exercices

### Exercice 1 : Variables Locales

**Objectif :** Comprendre qu'une variable locale n'existe que dans sa fonction.

La fonction `set_local()` :

- Définit une variable locale `y = 15`
- Affiche cette variable

**Question :** Que se passe-t-il si on essaie d'afficher `y` en dehors de la fonction ?

**Réponse :** Python lève une `NameError` car `y` n'existe que dans le scope de la fonction.

```python
def set_local():
    y = 15  # Variable locale
    print(f"y dans la fonction : {y}")

set_local()  # Fonctionne
print(y)     # ❌ NameError: name 'y' is not defined
```

### Exercice 2 : Variables Globales

**Objectif :** Comprendre comment modifier une variable globale depuis une fonction.

- Variable globale `z = 30`
- Fonction `modify_z()` qui modifie `z` à `50` avec le mot-clé `global`

```python
z = 30  # Variable globale

def modify_z():
    global z  # Important : déclare qu'on modifie la variable globale
    z = 50

print(z)      # Affiche 30
modify_z()
print(z)      # Affiche 50
```

**Note importante :** Sans le mot-clé `global`, Python créerait une nouvelle variable locale `z` dans la fonction, et la variable globale ne serait pas modifiée.

## Exécution

Pour exécuter le programme :

```bash
python variables_scope.py
```

Pour exécuter les tests :

```bash
python test_variables_scope.py
```

## Concepts clés

### Portée locale (Local Scope)

- Les variables définies dans une fonction n'existent que dans cette fonction
- Elles sont détruites à la fin de l'exécution de la fonction

### Portée globale (Global Scope)

- Les variables définies au niveau du module sont globales
- Elles sont accessibles partout dans le fichier
- Pour les modifier dans une fonction, il faut utiliser le mot-clé `global`

### Règle LEGB

Python cherche les variables dans cet ordre :

1. **L**ocal : dans la fonction actuelle
2. **E**nclosing : dans les fonctions englobantes
3. **G**lobal : au niveau du module
4. **B**uilt-in : dans les fonctions intégrées de Python
