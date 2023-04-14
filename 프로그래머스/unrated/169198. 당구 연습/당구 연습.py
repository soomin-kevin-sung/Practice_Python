def solution(m, n, startX, startY, balls):
    answer = []
    
    for ball in balls:
        # Candidates
        cands = []
        
        # Up
        if startX != ball[0] or startY > ball[1]:
            cands.append((startX - ball[0]) ** 2 + ((n - startY) + (n - ball[1])) ** 2)
        
        # Down
        if startX != ball[0] or startY < ball[1]:
            cands.append((startX - ball[0]) ** 2 + (startY + ball[1]) ** 2)
        
        # Left
        if startY != ball[1] or startX < ball[0]:
            cands.append((startX + ball[0]) ** 2 + (startY - ball[1]) ** 2)
        
        # Right
        if startY != ball[1] or startX > ball[0]:
            cands.append(((m - startX) + (m - ball[0])) ** 2 + (startY - ball[1]) ** 2)
        
        answer.append(min(cands))
        
    
    return answer