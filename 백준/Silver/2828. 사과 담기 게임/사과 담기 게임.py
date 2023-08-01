import sys

input = sys.stdin.readline
print = sys.stdout.write


def can_receive(apple):
    global basket_start, basket_end
    return basket_start <= apple <= basket_end


def move_basket(v):
    global basket_start, basket_end

    basket_start += v
    basket_end += v
    return abs(v)


n, m = map(int, input().split())
j = int(input())
basket_start = 1
basket_end = m
ans = 0

for _ in range(j):
    p = int(input())
    if p < basket_start:
        ans += move_basket(p - basket_start)
    elif p > basket_end:
        ans += move_basket(p - basket_end)

print(f'{ans}')
