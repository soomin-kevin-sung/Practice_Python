import sys

input = sys.stdin
output = sys.stdout

n = int(input.readline())
max_weights = []

ans = 0
for i in range(n):
    w = int(input.readline())

    ans = max(ans, w)
    ans = max()

