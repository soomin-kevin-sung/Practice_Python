import sys
from collections import deque

tree = []
n = 0


def get_most_far_node_with_dist(start):
    q = deque([start])
    dist = [-1] * (n + 1)
    dist[start] = 0

    while len(q) > 0:
        node = q.popleft()

        for next_node in tree[node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[node] + tree[node][next_node]
                q.append(next_node)

    return max([(i, dist[i]) for i in range(1, n + 1)], key=lambda t: t[1])


def main(input=sys.stdin, output=sys.stdout):
    global tree, n

    n = int(input.readline())
    tree = [{} for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b, c = map(int, input.readline().split())
        tree[a][b] = c
        tree[b][a] = c

    start, _ = get_most_far_node_with_dist(1)
    end, ans = get_most_far_node_with_dist(start)

    output.write(f'{ans}')


if __name__ == '__main__':
    main()
