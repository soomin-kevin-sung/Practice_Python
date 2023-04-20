import itertools

heights = []
for _ in range(9):
    heights.append(int(input()))

for c in itertools.combinations(heights, 7):
    if sum(c) == 100:
        for e in sorted(c):
            print(e)

        break
