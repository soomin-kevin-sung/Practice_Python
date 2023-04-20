heights = []
for _ in range(9):
    heights.append(int(input()))

answer = []
total = sum(heights)

for i in range(9):
    for j in range(i + 1, 9):
        tmp = total - heights[i] - heights[j]
        if tmp == 100:
            for k in range(9):
                if k == i or k == j:
                    continue

                answer.append(heights[k])

    if answer:
        break

answer.sort()

print('\n'.join(map(str, answer)))
