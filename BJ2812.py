import sys

input = sys.stdin
output = sys.stdout

n, k = map(int, input.readline().split())
s = list(input.readline().strip())

tmp = [(s[i], i) for i in range(n)]
tmp.sort()

for i in range(k):
    s[tmp[i][1]] = ''

for i in range(n):
    output.write(f'{s[i]}')
