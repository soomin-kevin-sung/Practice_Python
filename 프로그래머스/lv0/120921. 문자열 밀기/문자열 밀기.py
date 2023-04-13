def solution(A, B):
    l = len(A)
    
    for i in range(l):
        if A[0] == B[i]:
            flag = True
            
            for j in range(1, l):
                if A[j] != B[(i + j) % l]:
                    flag = False
                    break
                    
            if flag:
                return i
        
    return -1