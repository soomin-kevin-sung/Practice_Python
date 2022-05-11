import sys
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def main(input=sys.stdin, output=sys.stdout):
    max_row, max_col, pan, num_of_cheese = get_user_inputs()

    melting_hour, last_num_of_cheese = simulate(max_row, max_col, pan, num_of_cheese)

    output.write(f'{melting_hour}\n{last_num_of_cheese}')


def get_user_inputs(input=sys.stdin):
    r, c = map(int, input.readline().split())

    num_of_cheese = 0
    m = []
    for i in range(r):
        m.append(list(map(int, input.readline().split())))

        for j in range(c):
            if m[i][j] == 1:
                num_of_cheese += 1

    return r, c, m, num_of_cheese


def simulate(max_row, max_col, pan, num_of_cheese):
    global dx, dy

    vis = [[False for _ in range(max_col)] for _ in range(max_row)]
    dq = deque()
    dq.append((0, 0))

    hour_counter = 1
    while True:
        dq = melt_cheese(max_row, max_col, pan, dq, vis)

        if num_of_cheese - len(dq) == 0:
            return hour_counter, len(dq)

        num_of_cheese -= len(dq)
        hour_counter += 1


def melt_cheese(max_row, max_col, pan, dq, vis):
    global dx, dy
    # deque for next check location.
    next_dq = deque()

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            # if not visited
            if 0 <= tx < max_row and 0 <= ty < max_col and not vis[tx][ty]:
                vis[tx][ty] = True
                # if current location is cheese => melt and append to next check locations.
                if pan[tx][ty] == 1:
                    pan[tx][ty] = 0
                    next_dq.append((tx, ty))
                # else current location is air.
                elif pan[tx][ty] == 0:
                    # append to current check locations.
                    dq.append((tx, ty))

    return next_dq


if __name__ == '__main__':
    main()
