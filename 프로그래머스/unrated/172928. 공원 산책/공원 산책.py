def solution(park, routes):
    current = get_start(park)

    for route in routes:
        if not is_valid_route(park, current, route):
            continue

        run_route(current, route)

    return current


def is_valid_route(park, current, route):
    dir_dict = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
    pkts = route.split()

    w = len(park)
    h = len(park[0])

    nx = current[0]
    ny = current[1]

    for _ in range(int(pkts[1])):
        nx += dir_dict[pkts[0]][0]
        ny += dir_dict[pkts[0]][1]

        if not 0 <= nx < w or not 0 <= ny < h:
            return False
        elif park[nx][ny] == 'X':
            return False

    return True


def run_route(current, route):
    pkts = route.split()

    if pkts[0] == 'E':
        current[1] += int(pkts[1])
    elif pkts[0] == 'W':
        current[1] -= int(pkts[1])
    elif pkts[0] == 'S':
        current[0] += int(pkts[1])
    else:
        current[0] -= int(pkts[1])


def get_start(park):
    start = None
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                return [i, j]
