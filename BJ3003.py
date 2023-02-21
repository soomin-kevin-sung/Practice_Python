import sys


def main(input=sys.stdin, output=sys.stdout):
    k, q, l, b, kn, p = map(int, input.readline().split())
    output.write(f'{1 - k} {1 - q} {2 - l} {2 - b} {2 - kn} {8 - p}')


if __name__ == '__main__':
    main()
