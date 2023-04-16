def solution(sequence):
    sum_table = [0]
    
    d = 1
    for i in range(len(sequence)):
        sum_table.append(sum_table[-1] + sequence[i] * d)
        d *= -1
        
    return max(sum_table) - min(sum_table)