import sys
from collections import deque


def main(input=sys.stdin, output=sys.stdout):

    n, m = map(int, input.readline().split())
    targets = deque(map(int, input.readline().split()))
    q = deque([i for i in range(1, n + 1)])

    ans = get_path(q, targets)
    output.write(f'{ans}')


def get_path(q, targets):
    cnt = 0

    for target in targets:
        dist_cmd_2 = get_dist(2, q, target)
        dist_cmd_3 = get_dist(3, q, target)

        if dist_cmd_2 < dist_cmd_3:
            for _ in range(dist_cmd_2):
                do_cmd_2(q)

            cnt += dist_cmd_2
        else:
            for _ in range(dist_cmd_3):
                do_cmd_3(q)

            cnt += dist_cmd_3

        do_cmd_1(q)

    return cnt


def get_dist(d, q, n):
    cnt = 0
    len_of_q = len(q)

    # left
    if d == 2:
        return q.index(n)

    # right
    elif d == 3:
        return len_of_q - q.index(n)

    return 0


def do_cmd_1(q):
    if len(q) > 0:
        q.popleft()


def do_cmd_2(q):
    if len(q) > 0:
        v = q.popleft()
        q.append(v)


def do_cmd_3(q):
    if len(q) > 0:
        v = q.pop()
        q.appendleft(v)


if __name__ == '__main__':
    main()
