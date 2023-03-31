n = int(input())
m = int(input())
s = input()

pkts = []
cnt = 0

i = 2
while i < m:
    if s[i - 2] == 'I' and s[i - 1] == 'O' and s[i] == 'I':
        cnt += 1
        i += 1
    elif cnt:
        pkts.append(cnt)
        cnt = 0

    i += 1

if cnt:
    pkts.append(cnt)

ans = 0
for pkt in pkts:
    if pkt >= n:
        ans += pkt - (n - 1)

print(ans)