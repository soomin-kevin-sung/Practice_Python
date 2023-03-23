import sys
import heapq

input = sys.stdin
output = sys.stdout

n, k = map(int, input.readline().split())
items = []
bags = []

for _ in range(n):
    m, v = map(int, input.readline().split())
    items.append((m, v))

for _ in range(k):
    bags.append(int(input.readline()))

items.sort()
bags.sort()

hq = []
ans = 0
idx = 0

for bag in bags:
    while idx < n and items[idx][0] <= bag:
        heapq.heappush(hq, -items[idx][1])
        idx += 1

    if hq:
        ans -= hq[0]
        heapq.heappop(hq)

output.write(f'{ans}')
