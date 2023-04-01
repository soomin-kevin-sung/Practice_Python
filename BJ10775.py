import sys

# 푸는 중

input = sys.stdin
output = sys.stdout


def docking(dock, i):
    if dock[i] == i and dock[i] > 0:
        dock[i] = docking(dock, dock[i - 1])
    else:
        dock[i] = docking(dock, dock[i])

    return dock[i]


g = int(input.readline())
p = int(input.readline())

ans = 0
dock = [i for i in range(g + 1)]
for _ in range(p):
    gi = int(input.readline())
    if dock[gi]:
        docking(dock, gi)
    else:
        break

    ans += 1

output.write(f'{ans}')
