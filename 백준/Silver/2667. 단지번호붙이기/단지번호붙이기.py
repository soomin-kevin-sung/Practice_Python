import sys
input = sys.stdin.readline


def dfs(board, p):
    board[p[0]][p[1]] = '0'
    area = 1

    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_x = p[0] + d[0]
        next_y = p[1] + d[1]

        if (
                0 <= next_x < len(board) and
                0 <= next_y < len(board[next_x]) and
                board[next_x][next_y] == '1'
        ):
            area += dfs(board, (next_x, next_y))

    return area


n = int(input())
board = []
for _ in range(n):
    board.append(list(input().strip()))

num_of_site = 0
area = []
for i in range(n):
    for j in range(n):
        if board[i][j] == '1':
            area.append(dfs(board, (i, j)))
            num_of_site += 1

print(num_of_site)
print('\n'.join(map(str, sorted(area))))
