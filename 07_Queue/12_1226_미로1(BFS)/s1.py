import sys
from collections import deque
sys.stdin = open("input.txt")


def find(start):
    for i in range(N):
        for j in range(N):
            if start[i][j] == 2:
                return i, j


def find_way(x, y):
    visit[x][y] = True
    queue = deque([(x, y)])

    while queue:
        i, j = queue.popleft()

        for n in range(4):
            mx, my = i + dx[n], j + dy[n]
            if 0 <= mx < N and 0 <= my < N and not visit[mx][my]:
                if board[mx][my] == 3:
                    return 1
                elif board[mx][my] == 0:
                    queue.append((mx, my))
                visit[mx][my] = True
    return 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(10):
    print(f'#{input()}', end=' ')

    N = 16
    board = [list(map(int, input())) for _ in range(N)]
    visit = [[False] * N for _ in range(N)]
    i, j = find(board)
    print(find_way(i, j))

