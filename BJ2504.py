import sys


def pop_value(st, closed_char):
    if len(st) == 0:
        return -1

    params = {')': (2, '('),
              ']': (3, '[')}

    m, c = params[closed_char]

    if st[-1] == c:
        st.pop()
        return m

    ans = 0
    while len(st) > 0:
        item = st.pop()
        if type(item) is int:
            ans += item
        elif item == c:
            return ans * m
        else:
            return -1


def main(input=sys.stdin, output=sys.stdout):
    s = input.readline().strip()

    err = False
    closed_char = [')', ']']
    st = []
    for c in s:
        if c in closed_char:
            v = pop_value(st, c)
            if v == -1:
                st.append(None)
                break

            st.append(v)
        else:
            st.append(c)

    ans = 0
    for item in st:
        if type(item) is int:
            ans += item
        else:
            ans = 0
            break

    output.write(f'{ans}')


if __name__ == '__main__':
    main()
