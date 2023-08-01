import sys

input = sys.stdin.readline
print = sys.stdout.write


n, k = map(int, input().split())

l = 1
rs = []

while n >= 1:
    r = n % 2
    n //= 2

    if r == 1:
        rs.append(l)

    l *= 2

if len(rs) > k:
    print(f'{rs[-k] - sum(rs[:-k])}')
else:
    print('0')

