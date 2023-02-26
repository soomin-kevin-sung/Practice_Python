import sys

n = 0
cost = []
edges = []


def main(input=sys.stdin, output=sys.stdout):
    global n, cost, edges

    n = int(input.readline())

    cost = [{} for _ in range(n + 1)]
    edges = [{} for _ in range(n + 1)]
    for i in range(n - 1):
        a, b, v = map(int, input.readline().split())
        edges[a][b] = v
        edges[b][a] = v

    leaf = []
    for i in range(1, n + 1):
        if len(edges[i]) == 1:
            leaf.append(i)

    ans = []
    for node in leaf:
        ans.append(get_lowest_cost(1, node))

    ans.sort()
    if len(ans) > 2:
        output.write(f'{ans[0] + ans[1]}')
    else:
        output.write(f'{ans[0]}')


def get_lowest_cost(start, end):
    global n, cost, edges

    if end in cost[start]:
        return end
    else:
        for node in edges[start]:
            if node == end:
                cost[start][node] = edges[start][node]
            else:
                cost[node][end] = get_lowest_cost(node, end)
                cost[start][node] = edges[start][node] + cost[node][end]

    return cost[start][end]


if __name__ == '__main__':
    main()
