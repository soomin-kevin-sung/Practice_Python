import sys

input = sys.stdin
output = sys.stdout

n = int(input.readline())
weights = list(map(int, input.readline().split()))
weights.sort()

ans = -1
total = 1

for w in weights:
    if total < w:
        break

    total += w

output.write(f'{total}')
