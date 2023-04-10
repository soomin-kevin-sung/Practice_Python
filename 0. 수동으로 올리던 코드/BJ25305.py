import sys


def main(input=sys.stdin, output=sys.stdout):
    n, k = map(int, input.readline().split())
    scores = list(map(int, input.readline().split()))
    scores.sort(reverse=True)

    output.write(f'{scores[k - 1]}')


if __name__ == '__main__':
    main()

