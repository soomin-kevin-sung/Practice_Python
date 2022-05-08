# There is no limits an number operations.
# But the operation speed is slower when numbers bigger.

def main():
    while True:
        try:
            n = int(input())
            r = 1
            digit = 1
            while r % n:
                r %= n
                r = r * 10 + 1
                digit += 1

            print(digit)

        except EOFError:
            break


if __name__ == '__main__':
    main()
