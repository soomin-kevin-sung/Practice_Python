n, c = map(int, input().split())
m = int(input())

data = [list(map(int, input().split())) for _ in range(m)]
data.sort(key=lambda x: (x[1], -x[0]))

load = [0 for _ in range(n + 1)]
ans = 0
for d in data:
    if load[d[0]] < c:
        l = min(c - max(load[d[0]:d[1] + 1]), d[2])
        if l > 0:
            for i in range(d[0], d[1]):
                load[i] += l

            ans += l

print(ans)
