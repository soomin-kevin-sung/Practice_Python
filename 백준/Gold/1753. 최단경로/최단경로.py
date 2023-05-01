import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())

path = [{} for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    path[u].setdefault(v, 11)
    path[u][v] = min(path[u][v], w)

d = [INF for _ in range(V + 1)]
d[K] = 0
heap = [(0, K)]

while heap:
    dist, node = heapq.heappop(heap)
    if d[node] < dist:
        continue

    for c in path[node]:
        new_dist = path[node][c] + dist
        if new_dist < d[c]:
            d[c] = new_dist
            heapq.heappush(heap, (d[c], c))

print('\n'.join([str(e) if e != INF else 'INF' for e in d[1:]]))
