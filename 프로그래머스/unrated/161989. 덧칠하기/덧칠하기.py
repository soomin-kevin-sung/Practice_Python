from collections import deque

def solution(n, m, section):
    section = deque(section)    
    cnt = 0
    
    while section:
        node = section.popleft()
        while section and section[0] < node + m:
            section.popleft()
                
        cnt += 1
            
        
    return cnt