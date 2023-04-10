import sys
import math

n, m = 0, 0
table = []


def main(input=sys.stdin, output=sys.stdout):
    global n, m, table

    n, m = map(int, input.readline().split())

    for _ in range(n):
        table.append(list(input.readline().strip()))

    max_num = -1
    for i in range(n):
        for j in range(m):
            # 각 점을 돌면서 row_int, col_int에 따른 숫자들을 모두 판단한다.
            for row_int in range(-n + 1, n):
                for col_int in range(-m + 1, m):
                    nums = get_number(i, j, row_int, col_int)
                    for num in nums:
                        if math.sqrt(num).is_integer() and max_num < num:
                            max_num = num

    output.write(f'{max_num}')


def get_number(r, c, row_int, col_int):
    global n, m, table

    if row_int == 0 and col_int == 0:
        yield int(table[r][c])

    else:
        ans = ''

        while 0 <= r < n and 0 <= c < m:
            ans += table[r][c]
            r += row_int
            c += col_int

            yield int(ans)


if __name__ == '__main__':
    main()
