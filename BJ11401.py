def fact(x):
    num = 1

    for i in range(2, x + 1):
        num = (num * i) % p

    return num


def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x

    result = power(x, y // 2)
    if y % 2:
        result = pow(result, 2) * x
    else:
        result = pow(result, 2)

    return result % p


n, k = map(int, input().split())
p = 1000000007

a = fact(n) % p
b = power(fact(k) * fact(n - k) % p, p - 2) % p

print(a * b % p)


