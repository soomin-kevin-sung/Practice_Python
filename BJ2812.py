import sys
import heapq
from collections import deque

input = sys.stdin
output = sys.stdout

n, k = map(int, input.readline().split())
s = list(input.readline().strip())

t = n - k

hq = []
for i in range(n):
    heapq.heappush(hq, (-min(n - i, t), i, s[i]))

q = deque()
max_chr = '0'
ans = []

for i in range(t):
    while hq and -hq[0][0] == t - i:
        _, idx, c = heapq.heappop(hq)

        if max_chr < c:
            max_chr = c
            q.clear()
        else:
            heapq.heappush(q, (c, idx))

    ans.append(max_chr)
    max_chr = '0'


