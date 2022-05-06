def main():
    k, n, m = map(int, input().split())
    print(k * n - m if k * n > m else 0)


if __name__ == '__main__':
    main()
