n = int(input())

t = []
p = []
for i in range(n):
    ti, pi = map(int, input().split())

    if i + ti > n:
        pi = 0

    t.append(ti)
    p.append(pi)

answer = 0
d = [0 for _ in range(n + 1)]
for i in range(n - 1, -1, -1):
    a = d[i + 1] if i < n - 1 else 0
    b = d[i + t[i]] + p[i] if i + t[i] < n else p[i]

    d[i] = max(a, b)
    answer = max(answer, d[i])

print(answer)
