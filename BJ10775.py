import sys

# 푸는 중

input = sys.stdin
output = sys.stdout

g = int(input.readline())
p = int(input.readline())

s = set()
for _ in range(p):
    s.add(int(input.readline()))

output.write(f'{len(s)}')
