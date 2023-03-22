import sys

input = sys.stdin
output = sys.stdout

a, b = map(int, input.readline().split())

cnt = 0
while a < b:
    r = b % 10
    if r == 1:
        b //= 10
    elif r % 2 == 0:
        b //= 2
    else:
        break

    cnt += 1

output.write(f'{cnt + 1 if a == b else -1}')
