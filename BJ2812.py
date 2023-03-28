import sys

input = sys.stdin
output = sys.stdout

n, k = map(int, input.readline().split())
s = list(map(int, input.readline().strip()))

st = []
cnt = 0
for i in s:
    while st and st[-1] < i and cnt < k:
        st.pop()
        cnt += 1

    st.append(i)

output.write(f'{"".join(map(str, st[:n - k]))}')
