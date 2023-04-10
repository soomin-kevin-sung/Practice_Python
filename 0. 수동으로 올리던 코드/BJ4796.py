import sys

input = sys.stdin
output = sys.stdout

case = 1
while True:
    l, p, v = map(int, input.readline().split())

    if (l, p, v) == (0, 0, 0):
        break

    ans = (v // p) * l + min(l, v % p)
    output.write(f'Case {case}: {ans}\n')

    case += 1
