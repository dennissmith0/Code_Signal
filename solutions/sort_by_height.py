def solution(a):
    people = []
    for x in a:
        if x != -1:
            people.append(x)
            
    people.sort()   
    
    j = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = people[j]
            j += 1
            
    return a