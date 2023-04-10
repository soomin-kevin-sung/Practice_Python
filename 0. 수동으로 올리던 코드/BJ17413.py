import sys


def main(input=sys.stdin, output=sys.stdout):
    s = input.readline().strip()

    ans = ''

    idx = 0
    while idx < len(s):
        if s[idx] == '<':
            e_idx = s.find('>', idx)
            ans += s[idx:e_idx + 1]
            idx = e_idx + 1
        else:
            e_idx = s.find('<', idx)
            if e_idx == -1:
                e_idx = len(s)

            rev_strs = [elem[::-1] for elem in s[idx:e_idx].split(' ')]
            ans += ' '.join(rev_strs)
            idx = e_idx

    output.write(ans)


if __name__ == '__main__':
    main()
