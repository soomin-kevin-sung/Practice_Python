import sys
from collections import deque


def main():
    max_row, max_col, pan, num_of_cheese = get_user_inputs()

    simulate(max_row, max_col, pan, num_of_cheese)


def get_user_inputs(input=sys.stdin):
    r, c = map(int, input.readline().split())

    num_of_cheese = 0
    m = []
    for i in range(r):
        m.append(list(map(int, input.readline().split())))

        for elem in m[i]:
            if elem == 1:
                num_of_cheese += 1

    return r, c, m, num_of_cheese


def simulate(max_row, max_col, pan, num_of_cheese):
    dq = deque()
    dq.append((0, 0))

    fill_air(max_row, max_col, pan, dq)


def fill_air(max_row, max_col, pan, dq):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while dq:
        x, y = dq.popleft()
        pan[x][y] = 2

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < max_row and 0 <= ty < max_col and pan[tx][ty] == 0:
                dq.append((tx, ty))


if __name__ == '__main__':
    main()
