import sys

input = sys.stdin
output = sys.stdout

n = int(input.readline())
a = list(map(int, input.readline().split()))
b = list(map(int, input.readline().split()))


a.sort()
b.sort(reverse=True)

ans = 0
for i in range(n):
    ans += a[i] * b[i]

output.write(f'{ans}')