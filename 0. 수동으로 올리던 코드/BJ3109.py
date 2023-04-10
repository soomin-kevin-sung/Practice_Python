import sys

input = sys.stdin
output = sys.stdout

r, c = 0, 0
table = []
dr = [-1, 0, 1]


def exist_way_to_bakery(nr, nc):
    table[nr][nc] = 'm'

    if nc == c - 1:
        return True
    else:
        for d in dr:
            tr = nr + d
            tc = nc + 1
            if 0 <= tr < r and 0 <= tc < c and table[tr][tc] == '.':
                if exist_way_to_bakery(tr, tc):
                    return True

    return False


if __name__ == '__main__':
    r, c = map(int, input.readline().split())
    for _ in range(r):
        table.append(list(input.readline().strip()))

    ans = 0
    for i in range(r):
        if exist_way_to_bakery(i, 0):
            ans += 1

    output.write(f'{ans}')
