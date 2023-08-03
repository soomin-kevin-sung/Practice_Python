import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
q = []

for i in range(n):
    e = list(map(int, input().split()))
    for j in range(n):
        heapq.heappush(q, e[j])

        if len(q) > n:
            heapq.heappop(q)


ans = heapq.heappop(q)


print(f'{ans}')
