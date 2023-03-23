import sys

input = sys.stdin
output = sys.stdout

n, m = map(int, input.readline().split())
min_package_price = 1001
min_piece_price = 1001

for _ in range(m):
    a, b = map(int, input.readline().split())
    min_package_price = min(min_package_price, a)
    min_piece_price = min(min_piece_price, b)

if min_piece_price * 6 < min_package_price:
    output.write(f'{n * min_piece_price}')
else:
    output.write(f'{(n // 6) * min_package_price + min((n % 6) * min_piece_price, min_package_price)}')

