def solution(n):
    n_str = str(n)
    length = len(n_str)
    half_length = length // 2
    
    sum1 = 0
    sum2 = 0
    
    for i in range(0, half_length):
        sum1 += int(n_str[i])
        
    for i in range(half_length, length):
        sum2 += int(n_str[i])
        
    return sum1 == sum2
