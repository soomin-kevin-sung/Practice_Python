import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().split()
    for word in s:
        sys.stdout.write(f'{word[::-1]} ')

    sys.stdout.write('\n')
