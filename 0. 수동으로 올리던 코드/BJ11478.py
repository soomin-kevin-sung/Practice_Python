import sys


def main(input=sys.stdin, output=sys.stdout):
    s = input.readline().strip()

    h = {}
    for i in range(len(s)):
        for j in range(len(s)):
            if len(s) - j < i:
                break

            p = s[j:i+j]
            if p not in h:
                h[p] = None

    output.write(f'{len(h)}')


if __name__ == '__main__':
    main()

