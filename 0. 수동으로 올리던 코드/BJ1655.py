import sys
from heapq import heappush, heappop


def main(input=sys.stdin, output=sys.stdout):
    n = int(input.readline())

    left_heap = []
    right_heap = []

    for i in range(n):
        m = int(input.readline())

        if i % 2:
            heappush(right_heap, m)
        else:
            heappush(left_heap, -m)

        if len(left_heap) > 0 and len(right_heap) > 0:
            if -left_heap[0] > right_heap[0]:
                left = -heappop(left_heap)
                right = heappop(right_heap)

                heappush(left_heap, -right)
                heappush(right_heap, left)

        output.write(f'{-left_heap[0]}\n')


if __name__ == '__main__':
    main()
