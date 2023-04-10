def main():
    t = int(input())

    a = t // 300
    b = t % 300 // 60
    c = t % 60 // 10

    if t % 10:
        print(-1)
    else:
        print(a, b, c)


if __name__ == '__main__':
    main()
