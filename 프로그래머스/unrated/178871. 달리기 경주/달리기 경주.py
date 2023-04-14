def solution(players, callings):
    rank = {}
    
    for i in range(len(players)):
        rank[players[i]] = i
        
    for name in callings:
        call(players, rank, name)
    
    return list(players)


def call(players, rank, name):
    r1 = rank[name]
    
    r2 = r1 - 1
    name2 = players[r2]
    
    players[r1], players[r2] = players[r2], players[r1]
    rank[name] = r2
    rank[name2] = r1
    