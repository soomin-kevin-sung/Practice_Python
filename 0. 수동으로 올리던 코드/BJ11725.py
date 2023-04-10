import sys
from collections import deque


def main(input=sys.stdin, output=sys.stdout):
    n = int(input.readline())

    edges = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a, b = map(int, input.readline().split())
        edges[a].append(b)
        edges[b].append(a)

    parent = {1: 0}
    q = deque()
    q.append(1)

    while len(q) > 0:
        node = q.pop()

        for child in edges[node]:
            if child not in parent:
                parent[child] = node
                q.append(child)

    output.write('\n'.join(str(parent[i]) for i in range(2, n + 1)))


if __name__ == '__main__':
    main()
