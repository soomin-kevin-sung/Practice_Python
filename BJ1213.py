import sys

input = sys.stdin
output = sys.stdout


def create_palindrome(counter):
    ans = ''
    center = ''

    for c in sorted(counter):
        if counter[c] % 2:
            if center != '':
                return ''

            center = c

        ans += c * (counter[c] // 2)

    return ans + center + ans[::-1]


s = input.readline().strip()
counter = {}

for c in s:
    counter.setdefault(c, 0)
    counter[c] += 1

ans = create_palindrome(counter)
if ans == '':
    output.write('I\'m Sorry Hansoo')
else:
    output.write(ans)
