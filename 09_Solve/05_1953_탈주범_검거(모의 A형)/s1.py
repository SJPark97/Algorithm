from collections import deque
import sys

sys.stdin = open('input.txt')


def bfs(i, j, l):
    queue = deque([(i, j, l-1)])
    visit[i][j] = 1
    while queue:
        x, y, t = queue.popleft()
        a = board[x][y]
        for n in direction[a]:
            nx, ny = x + dx[n], y + dy[n]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] in chk[n] and visit[nx][ny] == 0 and t > 0:
                visit[nx][ny] = 1
                queue.append((nx, ny, t-1))


dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
direction = ((), (0, 1, 2, 3), (0, 1), (2, 3), (0, 3), (1, 3), (1, 2), (0, 2))
chk = ((1, 2, 5, 6), (1, 2, 4, 7), (1, 3, 4, 5), (1, 3, 6, 7))
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    bfs(R, C, L)
    print(sum(map(sum, visit)))