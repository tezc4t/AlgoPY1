

def bubble_sort(l):
    for i in range(len(l) - 1, 0, -1):
        j = 0
        while j < i:
            value = l[j]
            if value > l[j + 1]:
                temp = l[j + 1]
                l[j+1] = value
                l[j] = temp
            j += 1
            
    return l

            


print(bubble_sort([4,2,6,5,1,3]))

print("""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """)
 

 
 