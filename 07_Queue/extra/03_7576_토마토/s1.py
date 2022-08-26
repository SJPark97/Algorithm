import sys
from collections import deque
sys.stdin = open("input.txt")


def tomato(que):
    while que:
        x, y, t = que.popleft()
        for n in range(4):
            mx, my = x + dx[n], y + dy[n]
            if 0 <= mx < N and 0 <= my < M and board[mx][my] == 0:
                board[mx][my] = 1
                que.append((mx, my, t+1))

    for check_tomato in board:
        if 0 in tuple(check_tomato):
            return -1
    return t


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            queue.append((i, j, 0))

print(tomato(queue))

