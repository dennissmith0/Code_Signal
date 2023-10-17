def solution(inputString):
    char_count = {}
    
    for char in inputString:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    odd_char_count = 0
    
    for count in char_count.values():
        if count % 2 != 0:
            odd_char_count += 1
            
    if odd_char_count > 1:
        return False
        
    return True
