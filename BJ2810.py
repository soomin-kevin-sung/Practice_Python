n = int(input())
s = input()

idx = 0
ans = 0

while idx < n:
    if s[idx] == 'S':
        ans += 1
        idx += 1
    else:
        ans += 1
        idx += 2

print(min(n, ans + 1))
