def merge(l1, l2):
    combined = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        
        if l1[i] < l2[j]:
            combined.append(l1[i])
            i += 1 
        else:
            combined.append(l2[j])
            j += 1 
            
    while i < len(l1):
        combined.append(l1[i])
        i += 1
        
        
    while j < len(l2):
        combined.append(l2[j])
        j += 1

    return combined
            
    
print(merge([1,2,7,8], [3,4,5,6]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]
    
 """