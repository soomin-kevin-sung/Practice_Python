import sys

input = sys.stdin
output = sys.stdout

board = input.readline().strip()

i = 0
cnt = 0
ans = []

while i < len(board):
    while i < len(board) and board[i] == '.':
        ans.append('.')
        i += 1
        cnt = 0

    while i < len(board) and board[i] != '.':
        i += 1
        cnt += 1

    if cnt % 2 == 0:
        a = cnt // 4
        b = (cnt % 4) // 2
        ans.append(f'{"AAAA" * a}')
        ans.append(f'{"BB" * b}')
    else:
        ans = ['-1']
        break

output.write(f'{"".join(ans)}')
