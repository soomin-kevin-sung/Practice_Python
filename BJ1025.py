import sys

# 푸는 중

def main(input=sys.stdin, output=sys.stdout):
    n, m = map(int, input.readline().split())

    table = []
    for _ in range(n):
        table.append(list(map(int, list(input.readline().strip()))))

    for r in range(n):
        for row_int in range(n - r):
            rows = get_selection(r, n, row_int)
            if len(rows) == 1:
                rows = rows * m

            for c in range(m):
                for col_int in range(m - c):
                    cols = get_selection(c, m, col_int)
                    if len(cols) < len(rows):
                        continue

                    for i in range(len(cols)):
                        output.write(f'{table[rows[i]][cols[i]]}')

                    output.write('\n')


def get_selection(start, end, interval):
    if interval == 0:
        return [start]

    result = []

    item = start
    while item < end:
        result.append(item)
        item += interval

    return result


if __name__ == '__main__':
    main()
