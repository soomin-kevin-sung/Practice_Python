import sys

input = sys.stdin
output = sys.stdout

n = int(input.readline())
n = 1000 - n

coins = [500, 100, 50, 10, 5, 1]
ans = 0

for coin in coins:
    q = n // coin
    if q > 0:
        ans += q
        n %= coin

output.write(f'{ans}')
