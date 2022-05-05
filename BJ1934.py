def main():
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())

        print(a * b // gcd(a, b))


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


if __name__ == '__main__':
    main()
