import sys

input = sys.stdin
output = sys.stdout

n = int(input.readline())
cnt = [0] * 26

for _ in range(n):
    word = input.readline().strip()
    for i in range(len(word)):
        cnt[ord(word[i]) - 65] += 10 ** (len(word) - i - 1)

cnt.sort(reverse=True)

ans = 0
num = 9
for i in range(26):
    if cnt[i]:
        ans += cnt[i] * num
        num -= 1

output.write(f'{ans}')
