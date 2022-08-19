import sys
sys.setrecursionlimit(10000)


def dfs(x, y):
    visit[x][y] = True

    for n in range(4):
        nx = x + dx[n]
        ny = y + dy[n]
        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and board[nx][ny]:
            dfs(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(int(input())):
    M, N, K = map(int, input().split())

    board = [[0] * M for _ in range(N)]
    visit = [[False] * M for _ in range(N)]

    # dx = [-1, 1, 0, 0]
    # dy = [0, 0, -1, 1]
    count = 0

    for _ in range(K):
        y, x = map(int, input().split())
        board[x][y] = 1

    for i in range(N):
        for j in range(M):
            if board[i][j] and not visit[i][j]:
                dfs(i, j)
                count += 1

    print(count)
