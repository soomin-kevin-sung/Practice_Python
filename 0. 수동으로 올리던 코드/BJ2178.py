import sys
import queue

n, m = 0, 0


def get_can_go_points(maze, point):
    x, y = point

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    ans = []

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if nx < 0 or ny < 0 or nx >= n or ny >= m or maze[nx][ny] != 1:
            continue

        ans.append((nx, ny))

    return ans


def set_shortest_path_len(maze, path_len, startpoint):
    global n, m

    q = queue.Queue()
    q.put(startpoint)
    path_len[startpoint[0]][startpoint[1]] = 1

    while not q.empty():
        x, y = q.get()
        next_points = get_can_go_points(maze, (x, y))
        for next_x, next_y in next_points:
            if path_len[next_x][next_y] == 0 or path_len[next_x][next_y] > path_len[x][y] + 1:
                path_len[next_x][next_y] = path_len[x][y] + 1

                if (next_x, next_y) != (n - 1, m - 1):
                    q.put((next_x, next_y))


def main(input=sys.stdin, output=sys.stdout):
    global n, m

    n, m = map(int, input.readline().split())
    maze = [[] for _ in range(n)]
    path_len = [[0 for _ in range(m)] for _ in range(n)]

    for r in range(n):
        row = input.readline().strip()
        for e in row:
            maze[r].append(int(e))

    set_shortest_path_len(maze, path_len, (0, 0))

    output.write(f'{path_len[n - 1][m - 1]}')


if __name__ == '__main__':
    main()
