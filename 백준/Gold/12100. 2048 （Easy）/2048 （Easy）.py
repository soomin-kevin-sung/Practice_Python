import sys
input = sys.stdin.readline
output = sys.stdout.write

n = 0
table = []
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def get_next_pos(r, c, d):
    while True:
        next_r, next_c = r + dr[d], c + dc[d]
        if 0 <= next_r < n and 0 <= next_c < n:
            if table[next_r][next_c] != 0:
                return [r, c]
        else:
            return [r, c]

        r = next_r
        c = next_c


def get_order(d):
    if d < 2:
        start, stop, step = n - 1, -1, -1
    else:
        start, stop, step = 0, n, 1

    result = []
    for i in range(start, stop, step):
        for j in range(start, stop, step):
            if d % 2:
                if table[j][i] != 0:
                    result.append([j, i])
            else:
                if table[i][j] != 0:
                    result.append([i, j])

    return result


def dfs(depth):
    if depth == 5:
        return max([max(row) for row in table])
    else:
        result = 0

        for d in range(4):
            history = []
            merged = set()

            for r, c in get_order(d):
                next_r, next_c = get_next_pos(r, c, d)
                test_r, test_c = next_r + dr[d], next_c + dc[d]
                if (
                        0 <= test_r < n and
                        0 <= test_c < n and
                        table[test_r][test_c] == table[r][c] and
                        (test_r, test_c) not in merged
                ):
                    table[test_r][test_c] = table[r][c] * 2
                    table[r][c] = 0
                    history.append([r, c, test_r, test_c])
                    merged.add((test_r, test_c))
                else:
                    if [next_r, next_c] == [r, c]:
                        continue

                    table[next_r][next_c] = table[r][c]
                    table[r][c] = 0
                    history.append([r, c, next_r, next_c])

            if history:
                result = max(result, dfs(depth + 1))

                for r, c, next_r, next_c in reversed(history):
                    if (next_r, next_c) in merged:
                        table[r][c] = table[next_r][next_c] // 2
                        table[next_r][next_c] //= 2
                        merged.remove((next_r, next_c))
                    else:
                        table[r][c] = table[next_r][next_c]
                        table[next_r][next_c] = 0

        return result


n = int(input())
for _ in range(n):
    table.append(list(map(int, input().split())))

ans = dfs(0)
ans = ans if ans != 0 else max(max(row) for row in table)
output(f'{ans}')
