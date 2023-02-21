import sys


def main(input=sys.stdin, output=sys.stdout):
    n, m = map(int, input.readline().split())

    d = {}

    for _ in range(n):
        d[input.readline()] = None

    c = 0
    for _ in range(m):
        if input.readline() in d:
            c += 1

    output.write(f'{c}')


if __name__ == '__main__':
    main()
