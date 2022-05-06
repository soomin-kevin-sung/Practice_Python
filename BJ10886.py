def main():
    n = int(input())

    sum_of_vote = 0
    for _ in range(n):
        sum_of_vote += int(input())

    print('Junhee is cute!' if n / 2 < sum_of_vote else 'Junhee is not cute!')


if __name__ == '__main__':
    main()
