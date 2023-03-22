import sys

input = sys.stdin
output = sys.stdout

s = input.readline().strip()

cnt = {
    '0': 0,
    '1': 0
}

prev = ''
for c in s:
    if c != prev:
        cnt[c] += 1

    prev = c

ans = min(cnt['0'], cnt['1'])
output.write(f'{ans}')
