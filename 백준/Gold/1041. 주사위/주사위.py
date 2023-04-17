def get_dice_values(dice):
    comb = [
        [0, 1, 2, 3, 4, 5],
        [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)],
        [(0, 2, 1), (0, 3, 1), (0, 4, 2), (0, 3, 4), (5, 2, 4), (5, 3, 4), (5, 3, 1), (5, 1, 2)]
    ]

    result = []
    for i in range(3):
        min_value = 150
        max_element = 0
        for element in comb[i]:
            element = [dice[e] for e in ([element] if i == 0 else element)]
            sum_value = sum(element)
            if min_value > sum_value:
                min_value = sum_value
                max_element = max(element)
            elif min_value == sum_value:
                max_element = max(max_element, max(element))

        result.append((min_value, max_element))

    return result


n = int(input())
dice = list(map(int, input().split()))

if n == 1:
    print(sum(dice) - max(dice))
else:
    values = get_dice_values(dice)
    total_faces = [(n - 2) ** 2 * 6, (n - 2) * 12, 8]
    invisible_faces = [(n - 2) ** 2, (n - 2) * 4, 4]

    answer = 0
    for i in range(3):
        answer += total_faces[i] * values[i][0]
        answer -= invisible_faces[i] * values[i][1]

    print(answer)
