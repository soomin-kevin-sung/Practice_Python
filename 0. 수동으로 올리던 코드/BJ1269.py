import sys


def main(input=sys.stdin, output=sys.stdout):
    a, b = map(int, input.readline().split())

    A = list(map(int, input.readline().split()))
    B = list(map(int, input.readline().split()))

    A = {A[i]: None for i in range(len(A))}
    B = {B[i]: None for i in range(len(B))}

    c_ab = dict(A)
    for e in B:
        if e in c_ab:
            del c_ab[e]

    c_ba = dict(B)
    for e in A:
        if e in c_ba:
            del c_ba[e]

    output.write(f'{len(c_ab) + len(c_ba)}')


if __name__ == '__main__':
    main()
