def main():
    t = int(input())

    for _ in range(t):
        o, s = GetInputs()
        print(Solution(s, o))


def GetInputs():
    inputs = input().split()
    return int(inputs[0]), inputs[1]


def Solution(repeatString, numOfRepetitions):
    result = ''

    for c in repeatString:
        result += c * numOfRepetitions

    return result


if __name__ == '__main__':
    main()
