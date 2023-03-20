import sys

input = sys.stdin
output = sys.stdout

n = int(input.readline())
max_weights = []

for i in range(n):
    max_weights.append(int(input.readline()))

max_weights.sort()

ans = 0
for i in range(n):
    ans = max(ans, max_weights[i] * (n - i))

output.write(f'{ans}')
