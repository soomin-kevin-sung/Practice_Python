import heapq
import sys

input = sys.stdin.readline

n = int(input())
ranks = []

for _ in range(n):
    heapq.heappush(ranks, int(input()))

answer = 0
for i in range(n):
    answer += abs(heapq.heappop(ranks) - (i + 1))

print(answer)
