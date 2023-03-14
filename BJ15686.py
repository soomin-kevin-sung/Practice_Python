import sys

n, m = 0, 0
chicken_dists = []
homes = []
chickens = []
selected_chickens = []


def main(input=sys.stdin, output=sys.stdout):
    global n, m, chicken_dists, homes, chickens, selected_chickens

    n, m = map(int, input.readline().split())

    for i in range(n):
        row = list(map(int, input.readline().split()))

        for j in range(n):
            if row[j] == 1:
                homes.append((i, j))
                chicken_dists.append({})
            elif row[j] == 2:
                chickens.append((i, j))

    for i in range(len(homes)):
        for j in range(len(chickens)):
            chicken_dists[i][j] = get_distance(homes[i], chickens[j])

    output.write(f'{dfs(0)}')


def get_distance(home, chicken):
    return abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])


def dfs(idx):
    global chickens, selected_chickens

    if idx == m:
        return chicken_distance_of_city(selected_chickens)
    else:
        min_dist = 101
        for i in range(idx, len(chickens)):
            selected_chickens.append(i)

            dist = dfs(idx + 1)
            if min_dist > dist:
                min_dist = dist

            selected_chickens.pop()

        return min_dist


def chicken_distance_of_city(opened_chickens):
    global chicken_dists, homes

    ans = 0

    for home in range(len(homes)):
        dist = 101
        for chicken in opened_chickens:
            dist = min(dist, chicken_dists[home][chicken])

        ans += dist

    return ans


if __name__ == '__main__':
    main()
