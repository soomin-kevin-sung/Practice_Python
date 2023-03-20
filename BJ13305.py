import sys

input = sys.stdin
output = sys.stdout

n = int(input.readline())
dist_cost = list(map(int, input.readline().split()))
city_cost = list(map(int, input.readline().split()))

min_cost = city_cost[0]
ans = 0

for i in range(n - 1):
    if city_cost[i] < min_cost:
        min_cost = city_cost[i]

    ans += dist_cost[i] * min_cost

output.write(f'{ans}')

