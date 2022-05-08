def main():
    n, k = map(int, input().split())

    objects = []
    for _ in range(n):
        w, v = map(int, input().split())
        objects.append([w, v])

    dy = [0 for _ in range(k + 1)]

    for w, v in objects:
        for i in range(k, 0, -1):
            if i - w < 0:
                break

            dy[i] = max(dy[i - w] + v, dy[i])

    print(dy[k])


if __name__ == '__main__':
    main()
