def solution(inputArray):

    moves = 0
    
    for i in range(1, len(inputArray)):
        current = inputArray[i]
        prev = inputArray[i - 1]
        
        while current <= prev:
            current += 1
            moves += 1
        
        inputArray[i] = current
            
    return moves
