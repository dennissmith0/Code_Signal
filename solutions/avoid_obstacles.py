def solution(inputArray):
    max_obstacle = max(inputArray)
    
    for jump in range(2, max_obstacle + 2):
        is_valid_jump = True
        
        for coord in inputArray:
            if coord % jump == 0:
                is_valid_jump = False
                break
        
        if is_valid_jump:
            return jump
