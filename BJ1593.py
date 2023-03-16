import sys


def main(input=sys.stdin, output=sys.stdout):
    _ = input.readline()
    w = input.readline().strip()
    s = input.readline().strip()

    w_count = {}
    for c in w:
        count(w_count, c)

    ans = 0
    s_count = {}
    for i in range(len(s) - len(w) + 1):
        if i == 0:
            for c in s[0:len(w)]:
                count(s_count, c)
        else:
            discount(s_count, s[i - 1])
            count(s_count, s[i + len(w) - 1])

        if s_count == w_count:
            ans += 1

    output.write(f'{ans}')


def count(dct, key):
    if key not in dct:
        dct[key] = 0

    dct[key] += 1


def discount(dct, key):
    if key in dct:
        dct[key] -= 1

        if dct[key] <= 0:
            del dct[key]


if __name__ == '__main__':
    main()
