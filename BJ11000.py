import sys

# 푸는중

input = sys.stdin
output = sys.stdout

n = int(input.readline())
lectures = []

for _ in range(n):
    s, t = map(int, input.readline().split())
    lectures.append((s, t))

lectures.sort(key=lambda e: (e[0], e[1] - e[0]))


