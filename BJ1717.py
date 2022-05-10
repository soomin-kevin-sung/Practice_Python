import sys

sets = []


def main(input=sys.stdin, output=sys.stdout):
    global sets
    n, m = map(int, input.readline().split())

    sets = [-1 for i in range(n + 1)]

    for _ in range(m):
        o, a, b = map(int, input.readline().split())

        if o == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                output.write('YES\n')
            else:
                output.write('NO\n')


def union(a, b):
    global sets

    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        if sets[root_a] < sets[root_b]:
            sets[root_a] += sets[root_b]
            sets[root_b] = root_a
        else:
            sets[root_b] += sets[root_a]
            sets[root_a] = root_b


def find(x):
    global sets

    if sets[x] < 0:
        return x
    else:
        # Path Compression
        sets[x] = find(sets[x])
        return sets[x]


if __name__ == '__main__':
    main()
