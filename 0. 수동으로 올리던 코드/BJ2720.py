import sys

input = sys.stdin
output = sys.stdout

coin_types = (25, 10, 5, 1)


def solution(cost):
    for i in range(len(coin_types)):
        ans = cost // coin_types[i]
        cost %= coin_types[i]

        output.write(f'{ans} ')

    output.write('\n')


t = int(input.readline())

for _ in range(t):
    cost = int(input.readline())
    solution(cost)
