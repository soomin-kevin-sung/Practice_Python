import sys

input = sys.stdin
output = sys.stdout


n = int(input.readline())

max_sell = 0
best_seller = ''
data = {}

for _ in range(n):
    book = input.readline().strip()

    data.setdefault(book, 0)
    data[book] += 1

    if data[book] > max_sell or (data[book] == max_sell and book < best_seller):
        max_sell = data[book]
        best_seller = book

output.write(f'{best_seller}')
