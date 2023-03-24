import sys
import heapq

input = sys.stdin
output = sys.stdout

n = int(input.readline())
lectures = []

for _ in range(n):
    s, t = map(int, input.readline().split())
    lectures.append((s, t))

lectures.sort()
hq = []

ans = 0
for s, e in lectures:
    if hq and hq[0] <= s:
        heapq.heappop(hq)
        heapq.heappush(hq, e)
    else:
        heapq.heappush(hq, e)
        ans += 1

output.write(f'{ans}')
