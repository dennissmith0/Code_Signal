def solution(a, b):
    if a == b:
        return True
        
    diff_indices = []
    
    for i in range(len(a)):
        if a[i] != b[i]:
            diff_indices.append(i)
    
    if len(diff_indices) > 2:
        return False
    
    if len(diff_indices) == 2:
        i, j = diff_indices
        a[i], a[j] = a[j], a[i]
        if a == b:
            return True
        else:
            a[i], a[j] = a[j], a[i]
            return False

    if len(diff_indices) == 1:
        return False 
    
    return True 
