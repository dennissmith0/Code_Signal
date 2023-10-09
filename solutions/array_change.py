def solution(inputArray):

# Initialize the count of moves to 0
    moves = 0
    
    # Loop through the array starting from the second element
    for i in range(1, len(inputArray)):
        # Get the current and previous elements
        current = inputArray[i]
        prev = inputArray[i - 1]
        
        # Check if the current element is less than or equal to the previous element
        if current <= prev:
            # Calculate how much we need to increase current by
            diff = prev - current
            increment = diff + 1
            
            # Increment the current element directly
            current += increment
            
            # Add the increment value to the total moves
            moves += increment
        
        # Update the value of the current element in the array
        inputArray[i] = current
    
    return moves
