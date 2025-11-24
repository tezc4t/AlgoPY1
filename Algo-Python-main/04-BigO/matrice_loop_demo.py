
'''
python
liste = [1, 2, 3, 4, 5]
afficher_elements(liste)
# Affiche:
8 5
8 6
8 7
8 8
8 9
9 0
9 1
9 2
9 3
9 4
9 5
9 6
9 7
9 8
9 9
'''
def print_items(n):
    for i in range(n):            
        for j in range(n):
            print(i,j)
        
        

print_items(10)
