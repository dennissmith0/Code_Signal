def solution(inputArray):
    max_product = inputArray[0] * inputArray[1]
    
    for i in range(1, len(inputArray)-1):
        prod = inputArray[i] * inputArray[i+1]
        
        max_product = max(max_product, prod)
        
    return max_product

def solution(inputArray):
    biggest = None
    
    for i in range(len(inputArray) - 1):
        curr = inputArray[i] * inputArray[i+1]
        if biggest is None or curr > biggest:
             biggest = curr
    return biggest