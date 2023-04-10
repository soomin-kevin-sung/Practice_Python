def solution(name, yearning, photo):
    score = {}
    answer = []
    
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    
    for p in photo:
        total = 0
        for name_in_p in p:
            if name_in_p in score:
                total += score[name_in_p]
            
        answer.append(total)
    
    return answer