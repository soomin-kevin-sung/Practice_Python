import sys

n, m = 0, 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
board = []


def main(input=sys.stdin, output=sys.stdout):
    global n, m, board

    n, m = map(int, input.readline().split())

    for _ in range(n):
        board.append(list(input.readline().strip()))

    max_dist = -1

    for i in range(n):
        for j in range(m):
            if check_can_seacrh((i, j)):
                lands, _ = get_lands_and_max_dist((i, j))
                for node in lands:
                    if check_can_seacrh(node):
                        _, dist = get_lands_and_max_dist(node)
                        max_dist = max(max_dist, dist)

                erase_land(lands)

    output.write(f'{max_dist}')


def check_can_seacrh(p):
    global board

    # 육지의 꼭지점에서만 탐색하도록 조건 추가.
    return board[p[0]][p[1]] == 'L' and get_adjust_num_of_land(p) <= 2


def get_adjust_num_of_land(start):
    global n, m, board

    cnt = 0
    for i in range(4):
        x = start[0] + dx[i]
        y = start[1] + dy[i]

        if 0 <= x < n and 0 <= y < m and board[x][y] == 'L':
            cnt += 1

    return cnt


def get_lands_and_max_dist(start):
    global n, m, dx, dy, board

    q = [(start, 0)]
    appended = {start}
    idx = 0

    max_dist = -1

    while idx < len(q):
        item = q[idx]
        idx += 1

        xy = item[0]
        dist = item[1]

        if max_dist < dist:
            max_dist = dist

        for i in range(4):
            nx = xy[0] + dx[i]
            ny = xy[1] + dy[i]

            if (
                    0 <= nx < n and
                    0 <= ny < m and
                    (nx, ny) not in appended and
                    board[nx][ny] == 'L'
            ):
                q.append(((nx, ny), dist + 1))
                appended.add((nx, ny))

    return [node[0] for node in q], max_dist


def erase_land(lands):
    global n, m, board

    for node in lands:
        board[node[0]][node[1]] = 'W'


if __name__ == '__main__':
    main()
