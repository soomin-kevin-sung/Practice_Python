import sys

input = sys.stdin
output = sys.stdout


def push(item):
    q.append(item)

    idx = len(q) - 1

    while True:
        parent = (idx - 1) // 2
        if parent < 0 or q[idx] >= q[parent]:
            break

        q[idx], q[parent] = q[parent], q[idx]
        idx = parent


def pop():
    if len(q) == 0:
        return 0
    elif len(q) == 1:
        return q.pop()

    ans = q[0]

    idx = 0
    q[idx] = q.pop()
    heap_size = len(q)

    while True:
        left = idx * 2 + 1
        right = idx * 2 + 2

        exist_left = left < heap_size
        exist_right = right < heap_size

        if exist_left and exist_right and q[idx] > q[left] and q[idx] > q[right]:
            if q[left] < q[right]:
                q[idx], q[left] = q[left], q[idx]
                idx = left
            else:
                q[idx], q[right] = q[right], q[idx]
                idx = right
        elif exist_left and q[idx] > q[left]:
            q[idx], q[left] = q[left], q[idx]
            idx = left
        elif exist_right and q[idx] > q[right]:
            q[idx], q[right] = q[right], q[idx]
            idx = right
        else:
            break

    return ans


n = int(input.readline())
q = []

for _ in range(n):
    x = int(input.readline())
    if x:
        push(x)
    else:
        output.write(f'{pop()}\n')
