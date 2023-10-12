def solution(inputArray):
    max_length = 0
    longest_strings = []
    
    for string in inputArray:
        if len(string) > max_length:
            max_length = len(string)
            
    for string in inputArray:
        if len(string) == max_length:
            longest_strings.append(string)
            
    return longest_strings