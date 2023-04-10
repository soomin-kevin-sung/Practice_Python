def solution(sequence, k):
    left = 0
    sum_of_part = 0
    ans = [0, 999999]

    for right in range(len(sequence)):
        sum_of_part += sequence[right]

        while k < sum_of_part:
            sum_of_part -= sequence[left]
            left += 1

        if sum_of_part == k and ans[1] - ans[0] > right - left:
            ans = [left, right]

    return ans
