import sys
import heapq
INF = float('inf')
input = sys.stdin.readline

n = int(input())
m = int(input())

path = [{} for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    path[a].setdefault(b, INF)
    path[a][b] = min(path[a][b], c)

start, end = map(int, input().split())

costs = [INF] * (n + 1)
costs[start] = 0
heap = [(0, start)]

while heap:
    cost, node = heapq.heappop(heap)
    if costs[node] < cost:
        continue

    for e in path[node]:
        new_cost = path[node][e] + cost
        if new_cost < costs[e]:
            costs[e] = new_cost
            heapq.heappush(heap, (new_cost, e))

print(costs[end])