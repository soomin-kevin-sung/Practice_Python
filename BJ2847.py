import sys

input = sys.stdin
output = sys.stdout

n = int(input.readline())

scores = []
for _ in range(n):
    scores.append(int(input.readline()))

ans = 0
for i in range(n - 2, -1, -1):
    if scores[i + 1] <= scores[i]:
        ans += scores[i] - scores[i + 1] + 1
        scores[i] = scores[i + 1] - 1

output.write(f'{ans}')
