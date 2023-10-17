def solution(a):
    team1 = 0
    team2 = 0
    
    for i in range(0, len(a), 2):
        team1 += a[i]
        
    for j in range(1, len(a), 2):
        team2 += a[j]
        
    return [team1, team2]
