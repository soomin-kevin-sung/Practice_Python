import sys


def main(input=sys.stdin, output=sys.stdout):
    n = int(input.readline())
    cards = map(int, input.readline().split())
    m = int(input.readline())
    nums_for_check = map(int, input.readline().split())

    counter = {}
    for card in cards:
        if card not in counter:
            counter[card] = 0

        counter[card] += 1

    for num in nums_for_check:
        if num in counter:
            output.write(f'{counter[num]} ')
        else:
            output.write('0 ')


if __name__ == '__main__':
    main()
