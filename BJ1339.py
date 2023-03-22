import sys

input = sys.stdin
output = sys.stdout


def get_char_number_dict(words):
    digit_count = {}

    for word in words:
        for i in range(len(word)):
            c = word[i]

            if c not in digit_count:
                digit_count[c] = [0, 0]

            digit_count[c][0] = max(digit_count[c][0], len(word) - i)
            digit_count[c][1] += 1

    tuples = []
    for c in digit_count:
        data = digit_count[c]
        tuples.append((c, data[0], data[1]))

    tuples.sort(key=lambda t: (t[1], t[2], t[0]), reverse=True)

    key_number = {}

    for i in range(len(tuples)):
        key_number[tuples[i][0]] = 9 - i

    return key_number


# input n.
n = int(input.readline())
words = []

# input words.
for _ in range(n):
    words.append(input.readline().strip())

# get dict [char, number].
char_number_dict = get_char_number_dict(words)

# calculate.
ans = 0
for word in words:
    d = 10 ** (len(word) - 1)
    for c in word:
        ans += char_number_dict[c] * d
        d //= 10

# output ans.
output.write(f'{ans}')
