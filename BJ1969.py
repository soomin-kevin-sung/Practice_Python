import sys

input = sys.stdin
output = sys.stdout

n, m = map(int, input.readline().split())

dnas = []

for _ in range(n):
    dnas.append(input.readline().strip())

ans = ''
cnts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
dist = 0

for i in range(m):
    for j in range(n):
        cnts[dnas[j][i]] += 1

    max_cnt, max_key = 0, ''
    for c in cnts:
        if max_cnt < cnts[c]:
            max_cnt = cnts[c]
            max_key = c

        cnts[c] = 0

    ans += max_key
    dist += n - max_cnt

output.write(f'{"".join(ans)}\n{dist}')
