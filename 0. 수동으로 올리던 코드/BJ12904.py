import sys


def main(input=sys.stdin, output=sys.stdout):
    s = input.readline().strip()
    t = input.readline().strip()

    output.write(f'{1 if can_make_s_to_t(s, t) else 0}')


def can_make_s_to_t(s, t):
    while len(t):
        if t[-1] == 'A':
            t = rev_cmd(0, t)
        else:
            t = rev_cmd(1, t)

        if t == s:
            return True

    return False


def rev_cmd(option, t):
    if option == 0:
        return t[:-1]
    else:
        return t[:-1][-1::-1]


if __name__ == '__main__':
    main()
