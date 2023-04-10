import sys

k = 0


def merge_sort(a, p, r):

    if p < r:
        q = (p + r) // 2

        ans = merge_sort(a, p, q)
        if ans != -1:
            return ans

        ans = merge_sort(a, q + 1, r)
        if ans != -1:
            return ans

        return merge(a, p, q, r)

    return -1


def merge(a, p, q, r):
    global k

    i = p
    j = q + 1
    t = 0
    tmp = []

    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp.append(a[i])
            t += 1
            i += 1
        else:
            tmp.append(a[j])
            t += 1
            j += 1

    while i <= q:
        tmp.append(a[i])
        t += 1
        i += 1

    while j <= r:
        tmp.append(a[j])
        t += 1
        j += 1

    i = p
    t = 0
    while i <= r:
        k -= 1
        if k == 0:
            return tmp[t]

        a[i] = tmp[t]
        t += 1
        i += 1

    return -1


def main(input=sys.stdin, output=sys.stdout):
    global k

    n, k = map(int, input.readline().split())
    a = list(map(int, input.readline().split()))

    # worst case.
    # n = 500000
    # k = 200
    # a = [i for i in range(n, 0, -1)]

    ans = merge_sort(a, 0, n - 1)
    output.write(f'{ans}')


if __name__ == '__main__':
    main()
