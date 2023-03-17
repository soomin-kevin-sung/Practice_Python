import sys

# 푸는 중

input = sys.stdin
output = sys.stdout

n = int(input.readline())

meetings = []
for _ in range(n):
    s, e = map(int, input.readline().split())
    meetings.append((s, e))

meetings.sort(key=lambda t: (t[0], t[1] - t[0]))
output.write(f'{meetings}')

