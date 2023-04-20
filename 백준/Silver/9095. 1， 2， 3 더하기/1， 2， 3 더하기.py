t = int(input())
d = [0, 1, 2, 4, 7]
max_n = 4

for _ in range(t):
    n = int(input())
    while max_n < n:
        max_n += 1
        d.append(d[max_n - 3] + d[max_n - 2] + d[max_n - 1])

    print(d[n])
