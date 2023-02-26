import sys

n = 0
edges = []


def main(input=sys.stdin, output=sys.stdout):
    global n, edges

    n = int(input.readline())

    edges = [{} for _ in range(n + 1)]
    for i in range(n - 1):
        a, b, v = map(int, input.readline().split())
        edges[a][b] = v
        edges[b][a] = v

    leaf = []
    for i in range(1, n + 1):
        if len(edges[i]) == 1:
            leaf.append(i)

    if len(leaf) == 1:
        output.write(f'{get_lowest_cost(1, leaf[0])}')
    else:
        ans = []
        for node in leaf:
            ans.append((node, get_lowest_cost(1, node)))

        ans.sort(key=lambda t: t[1], reverse=True)

        output.write(f'{get_lowest_cost(ans[0][0], ans[1][0])}')


def get_lowest_cost(start, end):
    global n, edges

    lowest_cost = float('inf')
    for node in edges[start]:
        if node == end:
            lowest_cost = min(lowest_cost, edges[start][node])
        else:
            v = edges[node][start]
            del edges[node][start]

            lowest_cost = min(lowest_cost, edges[start][node] + get_lowest_cost(node, end))

            edges[node][start] = v

    return lowest_cost


if __name__ == '__main__':
    main()
