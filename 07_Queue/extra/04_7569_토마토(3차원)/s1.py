import sys
from collections import deque
sys.stdin = open("input.txt")


def tomato(que):
    while que:
        x, y, z, t = que.popleft()
        for n in range(6):
            mx, my, mz = x + dx[n], y + dy[n], z + dz[n]
            if 0 <= mx < N and 0 <= my < M and 0 <= mz < H and board[mz][mx][my] == 0:
                board[mz][mx][my] = 1
                que.append((mx, my, mz, t+1))

    for box in board:
        for check_tomato in box:
            if 0 in tuple(check_tomato):
                return -1
    return t


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque([])

for h in range(H):
    for i in range(N):
        for j in range(M):
            if board[h][i][j] == 1:
                queue.append((i, j, h, 0))

print(tomato(queue))

