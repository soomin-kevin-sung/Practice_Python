import sys

input = sys.stdin
output = sys.stdout

l = 5

board = [[0 for _ in range(l)] for _ in range(l)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

r = 2
c = 3
n = 2
dcnt = 1
cnt = 0
d = 0
total = 24

while total > 0:
    board[r][c] = n
    n += 1
    cnt += 1
    total -= 1

    r += dx[d]
    c += dy[d]

    if cnt == dcnt:
        cnt = 0
        d = (d + 1) % 4

        if d == 1 or d == 3:
            dcnt += 1


for i in range(l):
    for j in range(l):
        output.write(f'{board[i][j]:2} ')

    output.write('\n')