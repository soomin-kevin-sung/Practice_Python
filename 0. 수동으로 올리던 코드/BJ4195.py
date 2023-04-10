import sys

u = {}


def main(input=sys.stdin, output=sys.stdout):
    global u

    t = int(input.readline())

    for _ in range(t):
        f = int(input.readline())

        u = {}

        for i in range(f):
            a, b = input.readline().split()

            if u.get(a, 0) == 0:
                u[a] = 1

            if u.get(b, 0) == 0:
                u[b] = 1

            union(a, b)

            output.write(f'{u[find(a)]}\n')


def union(a, b):
    global u

    a = find(a)
    b = find(b)

    if a != b:
        if u[a] < u[b]:
            u[a] += u[b]
            u[b] = a
        else:
            u[b] += u[a]
            u[a] = b


def find(x):
    global u

    if isinstance(u[x], int):
        return x
    else:
        u[x] = find(u[x])
        return u[x]


if __name__ == '__main__':
    main()
