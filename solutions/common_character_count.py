def solution(s1, s2):
    count = 0
    s2_list = list(s2)
    
    for i in s1:
        if i in s2_list:
            count += 1
            s2_list.remove(i)
            
    return count
