d = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

n, m = map(int, input().split())
li = list([(list(map(lambda x: [d[c] for c in x], str(i))), i) for i in range(n, m + 1)])
li.sort()

for i in range(0, m - n + 1, 10):
    print(*list(map(lambda x: x[1], li[i:i + 10])))
