from collections import deque


n, k = map(int, input().split())
q = deque([(k, 0)])

v = {k}
answer = 0
while q:
    p, t = q.popleft()

    if p == n:
        answer = t
        break

    next_ps = [p - 1, p + 1]
    if p % 2 == 0:
        next_ps.append(p // 2)

    for next_p in next_ps:
        if next_p < 0 or next_p in v:
            continue

        q.append((next_p, t + 1))
        v.add(next_p)

print(answer)
