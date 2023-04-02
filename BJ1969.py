import sys

input = sys.stdin
output = sys.stdout

n, m = map(int, input.readline().split())

d = [{} for _ in range(m)]

for _ in range(n):
    dna = input.readline().strip()

    for i in range(m):
        d[i].setdefault(dna[i], 0)
        d[i][dna[i]] += 1

dist = 0
ans = ['Z' for _ in range(m)]
cnts = [0 for _ in range(m)]

for i in range(m):
    for c in d[i]:
        if cnts[i] <= d[i][c] and ans[i] > c:
            cnts[i] = d[i][c]
            ans[i] = c

    del d[i][ans[i]]

    for c in d[i]:
        dist += d[i][c]

output.write(f'{"".join(ans)}\n{dist}')
