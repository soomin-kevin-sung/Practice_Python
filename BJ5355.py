def main():
    t = int(input())

    for _ in range(t):
        inputs = input().split()

        o = float(inputs[0])

        print("%.2f" % Calculate(o, inputs[1:]))


def Calculate(operand, operators):
    for operator in operators:
        if operator == '@':
            operand *= 3
        elif operator == '%':
            operand += 5
        else:
            operand -= 7

    return operand


if __name__ == '__main__':
    main()
