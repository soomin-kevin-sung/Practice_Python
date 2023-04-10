import sys

p = [[0 for _ in range(100)] for _ in range(100)]


def main(input=sys.stdin, output=sys.stdout):
    global p

    area = 0

    t = int(input.readline())

    for _ in range(t):
        x, y = map(int, input.readline().split())

        for i in range(10):
            for j in range(10):
                if p[x + i][y + j] == 0:
                    p[x + i][y + j] = 1
                    area += 1

    output.write(f'{area}')


if __name__ == '__main__':
    main()
