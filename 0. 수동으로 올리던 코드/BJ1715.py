import sys
import heapq

input = sys.stdin
output = sys.stdout

n = int(input.readline())
deck = []

for _ in range(n):
    heapq.heappush(deck, int(input.readline()))

ans = 0

while len(deck) > 1:
    a = heapq.heappop(deck)
    b = heapq.heappop(deck)
    heapq.heappush(deck, a + b)

    ans += a + b

output.write(f'{ans}')

