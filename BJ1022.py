import sys


def main(input=sys.stdin, output=sys.stdout):
    r1, c1, r2, c2 = map(int, input.readline().split())

    nor = r2 - r1 + 1
    noc = c2 - c1 + 1

    board = [[0 for _ in range(noc)] for _ in range(nor)]

    # right bottom : n + 7 * (n - 1) + 4 * (n - 2)(n - 1)

    # for row in board:
    #     for cell in row:
    #         output.write(f'{cell:2} ')
    #     output.write('\n')


if __name__ == '__main__':
    main()
