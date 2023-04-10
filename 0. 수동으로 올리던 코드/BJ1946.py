import sys

input = sys.stdin
output = sys.stdout

t = int(input.readline())

for _ in range(t):
    n = int(input.readline())
    rank = [0] * (n + 1)

    for _ in range(n):
        a, b = map(int, input.readline().split())
        rank[a] = b

    ans = 1
    min_rank = rank[1]

    for e in rank[2:]:
        if min_rank > e:
            min_rank = e
            ans += 1

    output.write(f'{ans}\n')
