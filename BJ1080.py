import sys

input = sys.stdin
output = sys.stdout


def get_number_of_flip(a, b):
    a = [e[:] for e in a]
    b = [e[:] for e in b]
    cnt = 0

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != b[i][j]:
                if can_flip(a, i, j):
                    flip(a, i, j)
                    cnt += 1
                else:
                    return -1

    return cnt


def can_flip(m, x, y):
    row_len = len(m)
    col_len = len(m[0])

    if x + 3 > row_len:
        return False
    elif y + 3 > col_len:
        return False

    return True


def flip(m, x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            m[i][j] = '1' if m[i][j] == '0' else '0'


n, m = map(int, input.readline().split())

a = []
for _ in range(n):
    a.append(list(input.readline().strip()))

b = []
for _ in range(n):
    b.append(list(input.readline().strip()))

ans = get_number_of_flip(a, b)
output.write(f'{ans}')
