import sys
input = sys.stdin.readline
output = sys.stdout.write


n = int(input())
flowers = []

for _ in range(n):
    flower = list(map(int, input().split()))
    flowers.append((flower[0] * 100 + flower[1], flower[2] * 100 + flower[3]))

flowers.sort(key=lambda x: (x[0], -x[1]))
last = 301
last_idx = 0
c = 0

while last < 1201:
    max_last = 0
    for i in range(last_idx, n):
        if last < flowers[i][0]:
            break

        if max_last < flowers[i][1]:
            max_last = flowers[i][1]
            last_idx = i + 1

    if max_last:
        last = max_last
        c += 1
    else:
        break

if last >= 1201:
    output(f'{c}')
else:
    output('0')
