import sys
import heapq

input = sys.stdin
output = sys.stdout

n = int(input.readline())
hq = []

for _ in range(n):
    x = int(input.readline())

    if x == 0:
        output.write(f'{0 if len(hq) == 0 else -heapq.heappop(hq)}\n')
    else:
        heapq.heappush(hq, -x)
