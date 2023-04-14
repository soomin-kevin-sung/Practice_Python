from collections import deque


def solution(maps):
    maps = wrap_maps(maps)
    start, exit, lever = parse_params(maps)
    
    start_to_lever = bfs(maps, start, lever)
    if start_to_lever == -1:
        return -1
        
    lever_to_end = bfs(maps, lever, exit)
    if lever_to_end == -1:
        return -1
    
    return start_to_lever + lever_to_end


def wrap_maps(maps):
    new_maps = ['X' * (len(maps[0]) + 2)]
    for row in maps:
        new_maps.append('X' + row + 'X')
        
    new_maps.append('X' * (len(maps[0]) + 2))
    
    return new_maps


def parse_params(maps):
    start = None
    exit = None
    lever = None
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                start = i, j
            elif maps[i][j] == 'E':
                exit = i, j
            elif maps[i][j] == 'L':
                lever = i, j
                
    return start, exit, lever


def bfs(maps, start, target):
    vis = set()
    q = deque()
    q.append((start, 0))
    
    while q:
        p, cnt = q.popleft()
        
        if p == target:
            return cnt
        
        if p in vis:
            continue
            
        vis.add(p)
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            np = p[0] + d[0], p[1] + d[1]
            if maps[np[0]][np[1]] != 'X':
                q.append((np, cnt + 1))
        
    
    return -1