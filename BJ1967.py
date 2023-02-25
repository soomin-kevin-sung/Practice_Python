import sys

n = 0
cost = []
edges = []


def main(input=sys.stdin, output=sys.stdout):
    global n, cost, edges

    n = int(input.readline())

    cost = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
    edges = [{} for _ in range(n + 1)]
    for i in range(n - 1):
        a, b, v = map(int, input.readline().split())
        edges[a][b] = v
        edges[b][a] = v

    ans = 0
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            if s == e:
                continue
            ans = max(ans, get_lowest_cost(s, e))

    output.write(f'{ans}')


def get_lowest_cost(start, end):
    global n, cost, edges

    for node in edges[start]:
        if edges[start][node] == -1:
            continue

        if node == end:
            cost[start][end] = edges[start][node]
        else:
            del edges[node][start]
            c = get_lowest_cost(node, end)
            cost[start][end] = min(cost[start][end], c + edges[start][node])

            edges[node][start] = edges[start][node]

    return cost[start][end]


if __name__ == '__main__':
    main()
