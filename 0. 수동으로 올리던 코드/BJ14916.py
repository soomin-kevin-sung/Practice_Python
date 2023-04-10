import sys

input = sys.stdin
output = sys.stdout

n = int(input.readline())

t = n // 5

ans = -1
for i in range(t, -1, -1):
    if (n - 5 * i) % 2 == 0:
        ans = i + (n - 5 * i) // 2
        break

output.write(f'{ans}')
