import sys

# 푸는 중

input = sys.stdin
output = sys.stdout


def docking(dock, i):
    if dock[i] == i:
        return i
    else:
        dock[i] = docking(dock, dock[i])
        return dock[i]


g = int(input.readline())
p = int(input.readline())

ans = 0
dock = [i for i in range(g + 1)]
for _ in range(p):
    gi = int(input.readline())
    gate = docking(dock, gi)
    if not gate:
        break

    dock[gi] = docking(dock, gate - 1)
    ans += 1

output.write(f'{ans}')
