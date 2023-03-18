import sys

input = sys.stdin
output = sys.stdout

n = int(input.readline())

meetings = []
for _ in range(n):
    s, e = map(int, input.readline().split())
    meetings.append((s, e))

meetings.sort(key=lambda t: (t[1], t[0]))

ans = 0
e = 0

for meeting in meetings:
    if e <= meeting[0]:
        e = meeting[1]
        ans += 1

output.write(f'{ans}')

