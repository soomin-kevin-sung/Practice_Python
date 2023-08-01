import sys

input = sys.stdin.readline
print = sys.stdout.write


def dfs(v, start):
    c = 0

    if v == s and start > 0:
        c = 1

    for i in range(start, n):
        if used[i]:
            continue

        used[i] = True
        c += dfs(v + seq[i], i + 1)
        used[i] = False

    return c


n, s = map(int, input().split())
seq = list(map(int, input().split()))
used = [False for _ in range(n)]

print(f'{dfs(0, 0)}')
