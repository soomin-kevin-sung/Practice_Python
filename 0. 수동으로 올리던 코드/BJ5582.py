import sys


def main(input=sys.stdin, output=sys.stdout):
    a = input.readline().strip()
    b = input.readline().strip()

    carry = [0] * (len(b) + 1)

    ans = 0
    for i in range(1, len(a) + 1):
        dp = list(carry)

        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                carry[j] = dp[j - 1] + 1
                ans = max(ans, carry[j])
            else:
                carry[j] = 0

    output.write(f'{ans}')


if __name__ == '__main__':
    main()
