import sys
input = sys.stdin.readline

def union(u, a, b):
    a = find(u, a)
    b = find(u, b)

    if a == b:
        return

    if u[a] < u[b]:
        u[a] += u[b]
        u[b] = a
    else:
        u[b] += u[a]
        u[a] = b


def find(u, x):
    if u[x] < 0:
        return x
    else:
        return find(u, u[x])


n, m = map(int, input().split())
u = [-1 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(u, a, b)

print(sum(x < 0 for x in u[1:]))
