def solution(picture):
    result = []
    
    result.append("*" * (len(picture[0]) + 2))
    
    for row in picture:
        result.append("*" + row + "*")
        
    result.append("*" * (len(picture[0]) + 2))
    
    return result