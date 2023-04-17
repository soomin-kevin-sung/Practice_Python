n = int(input())

max_t = 0
assigns = []
for _ in range(n):
    t, s = map(int, input().split())
    assigns.append([t, s])
    max_t = max(t, max_t)

score = 0
for i in range(max_t, 0, -1):
    max_assign = [0, 0]
    for assign in assigns:
        if assign[0] >= i and assign[1] > max_assign[1]:
            max_assign = assign

    max_assign[0] = -1
    score += max_assign[1]

print(score)

