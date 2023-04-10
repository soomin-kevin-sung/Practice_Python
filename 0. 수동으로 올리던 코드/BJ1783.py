import sys

input = sys.stdin
output = sys.stdout

n, m = map(int, input.readline().split())

ans = 5 + m - 7
if n == 1 or m == 1:
    ans = 1
elif n < 3:
    ans = min(4, (m + 1) // 2)
elif m < 7:
    ans = min(4, m)

output.write(f'{ans}')
