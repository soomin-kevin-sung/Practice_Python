t = int(input())
for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))
    heights.sort()

    head = heights[0]
    tail = heights[1]
    i = 2
    ans = 0

    while i < n:
        if i == n - 1:
            ans = max(ans, abs(head - heights[i]), abs(tail - heights[i]))
        elif heights[i] < heights[i + 1]:
            ans = max(ans, abs(head - heights[i]), abs(tail - heights[i + 1]))
            head = heights[i]
            tail = heights[i + 1]
        else:
            ans = max(ans, abs(head - heights[i + 1]), abs(tail - heights[i]))
            head = heights[i + 1]
            tail = heights[i]

        i += 2

    print(ans)
