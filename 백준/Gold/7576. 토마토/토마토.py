from collections import deque


m, n = map(int, input().split())
num_of_tomatos = m * n

q = deque()
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] != 0:
            num_of_tomatos -= 1

            if board[i][j] == 1:
                q.append((i, j))


answer = 1
vis = set()
while q:
    node = q.popleft()
    if node in vis:
        continue

    vis.add(node)

    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_x = node[0] + d[0]
        next_y = node[1] + d[1]

        if (
                0 <= next_x < n and
                0 <= next_y < m and
                board[next_x][next_y] == 0
        ):
            num_of_tomatos -= 1
            board[next_x][next_y] = board[node[0]][node[1]] + 1
            q.append((next_x, next_y))

            answer = max(answer, board[next_x][next_y])

if num_of_tomatos:
    print(-1)
else:
    print(answer - 1)
