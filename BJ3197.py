import sys
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
nr, nc = 0, 0
lake = []
water_q = deque()
swan_q = deque()


def main(input=sys.stdin, output=sys.stdout):
    get_user_inputs(input)

    output.write(f'{simulate()}')


def get_user_inputs(input):
    global nr, nc, lake, water_q, swan_q
    nr, nc = map(int, input.readline().split())

    for i in range(nr):
        lake.append(list(input.readline().rstrip()))

        for j in range(nc):
            if lake[i][j] != 'X':
                water_q.append((i, j))

                if len(swan_q) == 0 and lake[i][j] == 'L':
                    swan_q.append((i, j))


def simulate():
    global nr, nc, lake, water_q, swan_q

    num_of_days = 0
    visited_swan = [[False for _ in range(nc)] for _ in range(nr)]
    visited_water = [[False for _ in range(nc)] for _ in range(nr)]

    visited_swan[swan_q[0][0]][swan_q[0][1]] = True

    while True:
        swan_q = find_swan(visited_swan)
        if swan_q is None:
            return num_of_days

        water_q = melt_ice(visited_water)
        num_of_days += 1


def find_swan(visited):
    global nr, nc, lake, water_q, swan_q
    next_q = deque()

    for x, y in swan_q:
        visited[x][y] = True

    while swan_q:
        x, y = swan_q.popleft()

        for d in range(4):
            tx = x + dx[d]
            ty = y + dy[d]

            if 0 <= tx < nr and 0 <= ty < nc and not visited[tx][ty]:
                visited[tx][ty] = True

                if lake[tx][ty] == '.':
                    swan_q.append((tx, ty))
                elif lake[tx][ty] == 'L':
                    return None
                else:
                    next_q.append((tx, ty))

    return next_q


def melt_ice(visited):
    global nr, nc, lake, water_q, swan_q
    next_q = deque()

    for x, y in water_q:
        visited[x][y] = True

    while water_q:
        x, y = water_q.popleft()

        for d in range(4):
            tx = x + dx[d]
            ty = y + dy[d]

            if 0 <= tx < nr and 0 <= ty < nc and not visited[tx][ty]:
                visited[tx][ty] = True

                if lake[tx][ty] == 'X':
                    lake[tx][ty] = '.'
                    next_q.append((tx, ty))
                else:
                    water_q.append((tx, ty))

    return next_q


if __name__ == '__main__':
    main()
