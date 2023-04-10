import sys


def main(input=sys.stdin, output=sys.stdout):
    x = int(input.readline())
    n = int(input.readline())

    v = 0
    for _ in range(n):
        a, b = map(int, input.readline().split())
        v += a * b

    output.write('Yes' if v == x else 'No')


if __name__ == '__main__':
    main()
