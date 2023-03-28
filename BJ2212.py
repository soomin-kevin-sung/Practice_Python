import sys

input = sys.stdin
output = sys.stdout

n = int(input.readline())
k = int(input.readline())
p = list(map(int, input.readline().split()))

p.sort()

d = []
for i in range(n - 1):
    d.append(p[i + 1] - p[i])

d.sort(reverse=True)
output.write(f'{sum(d[k - 1:])}')
