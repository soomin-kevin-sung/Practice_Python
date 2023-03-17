import sys
from collections import deque


def main(input=sys.stdin, output=sys.stdout):
    t = int(input.readline())

    while t:
        query = input.readline().strip()
        n = int(input.readline())
        q = input.readline().strip('[]\n')

        if q == '':
            q = deque()
        else:
            q = deque(q.split(','))

        ans = process(q, query)
        if ans != 'error':
            ans = f'[{",".join(ans)}]'

        output.write(f'{ans}\n')

        t -= 1


def process(dq, query):
    d = 1

    for cmd in query:
        if cmd == 'R':
            d *= -1
        else:
            if len(dq) == 0:
                return 'error'

            if d > 0:
                dq.popleft()
            else:
                dq.pop()

    ans = list(dq)
    return ans if d > 0 else ans[-1::-1]


if __name__ == '__main__':
    main()
