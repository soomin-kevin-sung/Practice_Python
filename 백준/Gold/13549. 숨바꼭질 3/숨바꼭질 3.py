from collections import deque

n, k = map(int, input().split())

q = deque([(n, 0)])
v = set()

ans = 100000
while q:
    p, t = q.popleft()
    if p in v:
        continue
    elif p == k:
        ans = min(ans, t)

    v.add(p)

    for np, nt in [(p * 2, t), (p - 1, t + 1), (p + 1, t + 1)]:
        if 0 <= np <= 100000:
            q.append((np, nt))

print(ans)
