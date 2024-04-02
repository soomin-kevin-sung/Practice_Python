import sys

input = sys.stdin.readline
output = sys.stdout.write

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())

r_pos = [0, 0]
b_pos = [0, 0]
o_pos = [0, 0]

table = []
for i in range(n):
    row = list(input().strip())
    for j in range(m):
        if row[j] == 'R':
            r_pos = [i, j]
        elif row[j] == 'B':
            b_pos = [i, j]
        elif row[j] == 'O':
            o_pos = [i, j]

    table.append(row)


def get_next_pos(r, c, d):
    while 0 <= r < n and 0 <= c < m:
        next_r = r + dr[d]
        next_c = c + dc[d]

        if table[next_r][next_c] == 'O':
            return [next_r, next_c]
        elif table[next_r][next_c] != '.':
            return [r, c]

        r = next_r
        c = next_c

    return None


def get_order(d):
    if d == 0:
        if r_pos[0] > b_pos[0]:
            return ['r', 'b']
        else:
            return ['b', 'r']
    elif d == 1:
        if r_pos[1] > b_pos[1]:
            return ['r', 'b']
        else:
            return ['b', 'r']
    elif d == 2:
        if r_pos[0] > b_pos[0]:
            return ['b', 'r']
        else:
            return ['r', 'b']
    elif d == 3:
        if r_pos[1] > b_pos[1]:
            return ['b', 'r']
        else:
            return ['r', 'b']


def dfs(depth, prev_d):
    global r_pos, b_pos, o_pos

    if r_pos == o_pos and b_pos != o_pos:
        return depth
    elif depth >= 10 or b_pos == o_pos:
        return -1
    else:
        result = -1

        for d in range(4):
            if d % 2 == prev_d % 2 and prev_d >= 0:
                continue

            prev_r_pos = r_pos
            prev_b_pos = b_pos

            is_moved = False
            for c in get_order(d):
                if c == 'r':
                    if table[r_pos[0]][r_pos[1]] != 'O':
                        table[r_pos[0]][r_pos[1]] = '.'

                    next_pos = get_next_pos(r_pos[0], r_pos[1], d)
                    is_moved |= next_pos != r_pos

                    r_pos = next_pos

                    if table[r_pos[0]][r_pos[1]] != 'O':
                        table[r_pos[0]][r_pos[1]] = 'R'
                else:
                    if table[b_pos[0]][b_pos[1]] != 'O':
                        table[b_pos[0]][b_pos[1]] = '.'

                    next_pos = get_next_pos(b_pos[0], b_pos[1], d)
                    is_moved |= next_pos != b_pos

                    b_pos = next_pos

                    if table[b_pos[0]][b_pos[1]] != 'O':
                        table[b_pos[0]][b_pos[1]] = 'B'

            if not is_moved:
                continue

            min_depth = dfs(depth + 1, d)
            if min_depth > 0:
                result = min(result, min_depth) if result > 0 else min_depth

            if table[r_pos[0]][r_pos[1]] != 'O':
                table[r_pos[0]][r_pos[1]] = '.'

            r_pos = prev_r_pos

            if table[r_pos[0]][r_pos[1]] != 'O':
                table[r_pos[0]][r_pos[1]] = 'R'

            if table[b_pos[0]][b_pos[1]] != 'O':
                table[b_pos[0]][b_pos[1]] = '.'

            b_pos = prev_b_pos

            if table[b_pos[0]][b_pos[1]] != 'O':
                table[b_pos[0]][b_pos[1]] = 'B'

        return result


output(f'{dfs(0, -1)}')
