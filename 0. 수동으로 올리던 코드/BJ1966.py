import sys
import queue


def get_print_order(q, doc_idx):
    order = 0

    while not q.empty():
        idx, pr = q.get()

        flag = False
        for it_idx, it_pr in q.queue:
            if pr < it_pr:
                flag = True
                break

        if flag:
            q.put((idx, pr))
        else:
            order += 1

            if idx == doc_idx:
                return order


def main(input=sys.stdin, output=sys.stdout):
    t = int(input.readline())

    for _ in range(t):
        n, m = map(int, input.readline().split())
        prs = list(map(int, input.readline().split()))

        q = queue.Queue()
        for i in range(n):
            q.put((i, prs[i]))

        output.write(f'{get_print_order(q, m)}\n')


if __name__ == '__main__':
    main()
