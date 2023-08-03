import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

q = []
n = int(input())

for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(q, (abs(x), x))
    else:
        print(f'{heapq.heappop(q)[1]}\n') if len(q) else print('0\n')
