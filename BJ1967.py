import sys

cost = []


def main(input=sys.stdin, output=sys.stdout):
    global cost

    n = int(input.readline())

    cost = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    edges = [{} for _ in range(n + 1)]
    for i in range(n - 1):
        a, b, v = map(int, input.readline().split())
        edges[a][b] = v
        edges[b][a] = v


def get_lowest_cost(edges, s, e):
    global cost

    for node in edges[s]:
        pass


if __name__ == '__main__':
    main()
