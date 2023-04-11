from collections import deque


def solution(board):
    answer = bfs(board)
    return answer


def bfs(board):
    board = wrap_board(board)

    vis = [[False] * len(board[0]) for _ in range(len(board))]
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = deque()

    start = get_start(board)
    q.append((start[0], start[1], 0))
    vis[start[0]][start[1]] = True

    while q:
        node = q.popleft()
        if board[node[0]][node[1]] == 'G':
            return node[2]

        for d in dirs:
            if board[node[0] + d[0]][node[1] + d[1]] != 'D':
                npos = get_move_pos(board, (node[0], node[1]), d)
                if not vis[npos[0]][npos[1]]:
                    vis[npos[0]][npos[1]] = True
                    q.append((npos[0], npos[1], node[2] + 1))
                    
    return -1


def get_start(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                return i, j


def wrap_board(board):
    ans = ['D' * (len(board[0]) + 2)]
    for row in board:
        ans.append('D' + row + 'D')

    ans.append('D' * (len(board[0]) + 2))
    return ans


def get_move_pos(board, pos, d):
    npos = [pos[0], pos[1]]
    while True:
        if board[npos[0] + d[0]][npos[1] + d[1]] == 'D':
            return npos

        npos[0] += d[0]
        npos[1] += d[1]
        