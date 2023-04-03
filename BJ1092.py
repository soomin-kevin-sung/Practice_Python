import heapq
import sys

n = int(input())
crains = list(map(int, input().split()))
m = int(input())
weights = list(map(int, input().split()))

crains.sort(reverse=True)
weights.sort(reverse=True)

heap = []
for weight in weights:
    heapq.heappush(heap, -weight)

ans = 0
while heap:
    for crain in crains:
        next_q = []

        while heap:
            w = -heapq.heappop(heap)
            if crain >= w:
                break

            next_q.append(w)

        for item in next_q:
            heapq.heappush(heap, -item)

    ans += 1

print(ans)
