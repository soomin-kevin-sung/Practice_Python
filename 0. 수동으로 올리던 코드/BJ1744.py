import sys
import heapq

input = sys.stdin
output = sys.stdout

n = int(input.readline())
pos = []
neg = []
ans = 0

for _ in range(n):
    num = int(input.readline())

    if num <= 0:
        neg.append(num)
    elif num == 1:
        ans += 1
    else:
        pos.append(num)

pos.sort(reverse=True)
neg.sort()

for i in range(len(pos)):
    if i % 2:
        ans += pos[i - 1] * pos[i]
    elif i == len(pos) - 1:
        ans += pos[i]

for i in range(len(neg)):
    if i % 2:
        ans += neg[i - 1] * neg[i]
    elif i == len(neg) - 1:
        ans += neg[i]

output.write(f'{ans}')
