from collections import deque


def simulate(board, viruses, num_of_blanks):
    q = deque()
    v = set()

    for virus in viruses:
        q.append(virus)

    while q:
        node = q.popleft()
        if node in v:
            continue

        v.add(node)
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = node[0] + d[0], node[1] + d[1]
            if 0 <= nx < len(board) and 0 <= ny < len(board[nx]) and board[nx][ny] == 0:
                q.append((nx, ny))

    return num_of_blanks - (len(v) - len(viruses))


n, m = map(int, input().split())
board = []

viruses = []
num_of_blanks = 0
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 0:
            num_of_blanks += 1
        elif board[i][j] == 2:
            viruses.append((i, j))

pos = []
for i in range(n):
    for j in range(m):
        pos.append((i, j))


answer = 0

for i in range(n * m):
    w1 = pos[i]
    if board[w1[0]][w1[1]] != 0:
        continue

    board[w1[0]][w1[1]] = 1

    for j in range(i, n * m):
        w2 = pos[j]
        if board[w2[0]][w2[1]] != 0:
            continue

        board[w2[0]][w2[1]] = 1

        for k in range(j, n * m):
            w3 = pos[k]
            if board[w3[0]][w3[1]] != 0:
                continue

            board[w3[0]][w3[1]] = 1

            answer = max(answer, simulate(board, viruses, num_of_blanks - 3))

            board[w3[0]][w3[1]] = 0
        board[w2[0]][w2[1]] = 0
    board[w1[0]][w1[1]] = 0

print(answer)
