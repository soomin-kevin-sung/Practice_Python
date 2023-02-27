import sys
from collections import deque

tree = []
v = 0


def get_most_far_node_with_dist(start):
    q = deque([start])
    dist = {start: 0}

    while len(q) > 0:
        node = q.popleft()

        for next_node in tree[node]:
            if next_node not in dist:
                dist[next_node] = dist[node] + tree[node][next_node]
                q.append(next_node)

    return max([(key, dist[key]) for key in dist.keys()], key=lambda t: t[1])


def main(input=sys.stdin, output=sys.stdout):
    global tree, v

    v = int(input.readline())
    tree = [{} for _ in range(v + 1)]

    for _ in range(v):
        args = list(map(int, input.readline().split()))
        p = args[0]

        for i in range(1, len(args) - 1, 2):
            c = args[i]
            v = args[i + 1]
            tree[p][c] = v

    start, _ = get_most_far_node_with_dist(1)
    end, ans = get_most_far_node_with_dist(start)

    output.write(f'{ans}')


if __name__ == '__main__':
    main()
