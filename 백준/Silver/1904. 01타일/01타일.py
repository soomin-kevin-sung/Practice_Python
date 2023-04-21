n = int(input())
d = [0, 1, 2, 3, 5]
for i in range(4, n + 1):
    d[i % 5] = (d[(i - 2) % 5] + d[(i - 1) % 5]) % 15746

print(d[n % 5])
