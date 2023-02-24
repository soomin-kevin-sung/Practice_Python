import sys


def main(input=sys.stdin, output=sys.stdout):
    n, m = map(int, input.readline().split())

    name_by_idx = {}
    idx_by_name = {}

    for i in range(n):
        name = input.readline().strip()
        name_by_idx[i + 1] = name
        idx_by_name[name] = i + 1

    for i in range(m):
        o = input.readline().strip()

        if o.isdigit():
            output.write(f'{name_by_idx[int(o)]}\n')
        else:
            output.write(f'{idx_by_name[o]}\n')


if __name__ == '__main__':
    main()
