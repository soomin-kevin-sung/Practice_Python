import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline
output = sys.stdout.write

vis = set()
graph = defaultdict(list)


def dfs_tracer(node):
    output(f'{node} ')
    vis.add(node)

    for next_node in graph[node]:
        if next_node in vis:
            continue

        dfs_tracer(next_node)


def bfs_tracer(node):
    q = deque([node])
    vis = set()

    while q:
        node = q.popleft()
        if node in vis:
            continue

        output(f'{node} ')
        vis.add(node)

        for next_node in graph[node]:
            q.append(next_node)


n, m, v = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()

dfs_tracer(v)
output('\n')
bfs_tracer(v)
