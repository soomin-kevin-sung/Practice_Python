import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
q = deque(map(int, input().split()))

st = deque()

i = 1
while i <= n:
    if len(q) and q[0] == i:
        q.popleft()
        i += 1
    else:
        if len(st) and st[-1] == i:
            st.pop()
            i += 1
        else:
            if len(q):
                st.append(q.popleft())
            else:
                break

if len(st) or len(q):
    output('Sad')
else:
    output('Nice')
