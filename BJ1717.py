import sys

input = sys.stdin
output = sys.stdout


def find_parent(x):
    if d[x] == x:
        return x
    else:
        d[x] = find_parent(d[x])
        return d[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        return

    if r[a] < r[b]:
        d[a] = b
    else:
        d[b] = a

        if r[a] == r[b]:
            r[a] += 1


n, m = map(int, input.readline().split())

d = [i for i in range(n + 1)]
r = [0 for _ in range(n + 1)]

for _ in range(m):
    c, a, b = map(int, input.readline().split())

    if c == 0:
        union(a, b)
    else:
        output.write(f'{"YES" if find_parent(a) == find_parent(b) else "NO"}\n')
