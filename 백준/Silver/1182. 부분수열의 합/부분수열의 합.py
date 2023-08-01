import sys

input = sys.stdin.readline
print = sys.stdout.write


def dfs(v, i):
    c = 0

    if i < n:
        c += dfs(v, i + 1)
        c += dfs(v + seq[i], i + 1)
        if v + seq[i] == s:
            c += 1

    return c


n, s = map(int, input().split())
seq = list(map(int, input().split()))

print(f'{dfs(0, 0)}')
