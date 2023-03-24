import sys
from collections import deque

# 푸는 중 (20%에서 틀림)

input = sys.stdin
output = sys.stdout


def get_release_concent(levels):
    last_obj = 0
    last_level = 0
    for used_obj in used:
        if levels[used_obj]:
            if levels[used_obj][0] > last_level:
                last_level = levels[used_obj][0]
                last_obj = used_obj
        else:
            last_level = 101
            last_obj = used_obj

    return last_obj


n, k = map(int, input.readline().split())
order = list(map(int, input.readline().split()))

levels = [deque() for _ in range(k + 1)]

for i in range(k):
    levels[order[i]].append(i)

cnt = 0
used = set()

for level in range(k):
    obj = order[level]

    if obj in used:
        continue
    elif len(used) < n:
        used.add(obj)
        if levels[obj]:
            levels[obj].popleft()
    else:
        rel_obj = get_release_concent(levels)
        used.remove(rel_obj)
        used.add(obj)

        cnt += 1

output.write(f'{cnt}')
