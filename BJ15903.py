import sys
import heapq

input = sys.stdin
output = sys.stdout

n, m = map(int, input.readline().split())
nums = list(map(int, input.readline().split()))
heap = []

for num in nums:
    heapq.heappush(heap, num)

for i in range(m):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    heapq.heappush(heap, a + b)
    heapq.heappush(heap, a + b)

output.write(f'{sum(heap)}')
