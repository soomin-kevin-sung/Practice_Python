import sys

input = sys.stdin
output = sys.stdout

t = int(input.readline())
for _ in range(t):
    n = int(input.readline())
    costs = list(map(int, input.readline().split()))

    num_of_buy = 0
    sum_of_buy_costs = 0
    sell_cost = -1
    ans = 0

    for cost in costs[::-1]:
        if sell_cost < cost:
            ans += sell_cost * num_of_buy - sum_of_buy_costs

            sell_cost = cost
            num_of_buy = 0
            sum_of_buy_costs = 0
        else:
            sum_of_buy_costs += cost
            num_of_buy += 1

    ans += sell_cost * num_of_buy - sum_of_buy_costs

    output.write(f'{ans}\n')
