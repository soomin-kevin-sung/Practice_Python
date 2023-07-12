import sys
input = sys.stdin.readline
output = sys.stdout.write

n, w = map(int, input().split())
costs = []
for _ in range(n):
    costs.append(int(input()))

if n > 1:
    coin = 0
    for i in range(0, n - 1):
        if costs[i] > costs[i + 1]:
            w += coin * costs[i]
            coin = 0
        else:
            coin += w // costs[i]
            w -= w // costs[i] * costs[i]

    if coin > 0:
        w += coin * costs[-1]

output(f'{w}')
