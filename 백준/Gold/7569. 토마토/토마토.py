import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

m, n, h = map(int, input().split())

# input tables and enqueue
q = deque()
box = []
num_of_yet = 0
for i in range(h):
    layer = []
    for j in range(n):
        row = list(map(int, input().split()))
        layer.append(row)

        for k in range(m):
            if row[k] == 1:
                q.append((i, j, k, 0))
            elif row[k] == 0:
                num_of_yet += 1

    box.append(layer)

d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1)]
ans = 0

num_of_enq = 0
while q:
    node = q.popleft()
    day = node[3]
    ans = max(ans, day)

    for di in d:
        x, y, z = node[0] + di[0], node[1] + di[1], node[2] + di[2]
        if 0 <= x < h and 0 <= y < n and 0 <= z < m:
            if box[x][y][z] == 0:
                box[x][y][z] = 1
                q.append((x, y, z, day + 1))
                num_of_enq += 1


print(f'{ans}' if num_of_yet == num_of_enq else '-1')
