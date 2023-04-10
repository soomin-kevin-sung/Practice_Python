import sys


def main(input=sys.stdin, output=sys.stdout):
    n = int(input.readline())
    cards = dict.fromkeys(map(int, input.readline().split()))
    m = int(input.readline())

    check_nums = map(int, input.readline().split())
    for num in check_nums:
        if num in cards:
            output.write('1 ')
        else:
            output.write('0 ')


if __name__ == '__main__':
    main()
