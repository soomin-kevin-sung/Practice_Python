import sys
output = sys.stdout.write

n, k = map(int, input().split())

output('<')

idx = k - 1
e = [i for i in range(1, n + 1)]

while True:
    output(f'{e[idx]}' if len(e) == n else f', {e[idx]}')
    del e[idx]

    if not e:
        break

    idx = (idx + k - 1) % len(e)

output('>')
