import sys
from collections import deque

input = sys.stdin
output = sys.stdout


def get_release_concent(used, levels):
    last_obj = 0
    last_level = 0
    for used_obj in used:
        if levels[used_obj]:
            if levels[used_obj][0] > last_level:
                last_level = levels[used_obj][0]
                last_obj = used_obj
        else:
            last_obj = used_obj
            break

    return last_obj


def get_release_count(order):
    k = len(order)
    levels = [deque() for _ in range(k + 1)]

    for i in range(k):
        levels[order[i]].append(i)

    cnt = 0

    used = set()
    for obj in order:
        if obj not in used:
            if len(used) < n:
                used.add(obj)
            else:
                rel_obj = get_release_concent(used, levels)
                used.remove(rel_obj)
                used.add(obj)

                cnt += 1

        if levels[obj]:
            levels[obj].popleft()

    return cnt


n, k = map(int, input.readline().split())
order = list(map(int, input.readline().split()))

ans = get_release_count(order)

output.write(f'{ans}')
