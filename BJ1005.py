import sys

# need set when submit python3
# sys.setrecursionlimit(10**6)

n = 0
k = 0
times = []
rels = []
w = 0
dy = []


def main(input=sys.stdin, output=sys.stdout):
    global n, k, times, rels, w, dy

    t = int(input.readline())

    for _ in range(t):
        user_input()

        dy = [-1 for _ in range(n)]
        output.write(f'{get_shortest_time(w)}\n')


def user_input(input=sys.stdin):
    global n, k, times, rels, w

    n, k = map(int, input.readline().split())
    times = [0] + list(map(int, input.readline().split()))

    n += 1

    rels = [[] for _ in range(n)]
    for i in range(k):
        a, b = map(int, input.readline().split())
        rels[b].append(a)

    w = int(input.readline())


def get_shortest_time(b):
    global n, k, times, rels, w, dy

    if dy[b] == -1:
        dy[b] = times[b]

        for e in rels[b]:
            dy[b] = max(dy[b], get_shortest_time(e) + times[b])

    return dy[b]


if __name__ == '__main__':
    main()
