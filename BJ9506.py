def main():
    while True:
        n = int(input())
        if n == -1:
            break

        divisors = get_perfect_number_divisors(n)
        if divisors is not None:
            print_perfect_number_and_divisors(n, divisors)
        else:
            print(n, 'is NOT perfect.')


def get_perfect_number_divisors(number):
    result = []
    sum_of_divisors = 0

    for i in range(1, number):
        if not number % i:
            sum_of_divisors += i
            result.append(i)

    if sum_of_divisors == number:
        return result

    return None


def print_perfect_number_and_divisors(number, divisors):
    print(number, '=', end=' ')
    print(*divisors, sep=' + ')


if __name__ == '__main__':
    main()
