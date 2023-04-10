import sys
from collections import deque

input = sys.stdin
output = sys.stdout

n, l = map(int, input.readline().split())
pos = list(map(int, input.readline().split()))

pos.sort()
pos = deque(pos)

cnt = 0
while pos:
    start = pos.popleft()

    while pos and pos[0] < start + l:
        pos.popleft()

    cnt += 1

output.write(f'{cnt}')
