import sys

input = sys.stdin
output = sys.stdout

n = int(input.readline())
p = list(map(int, input.readline().split()))

p.sort()
ans = 0

for i in range(n):
    ans += sum(p[:i + 1])

output.write(f'{ans}')