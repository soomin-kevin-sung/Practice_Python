def solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: x[1])

    lst = []
    for plan in plans:
        for i in range(len(lst)):
            if lst[i][0] > plan[1]:
                lst[i][0] += plan[2]

        lst.append([plan[1] + plan[2], plan[0]])

    lst.sort()
    return list(map(lambda x: x[1], lst))