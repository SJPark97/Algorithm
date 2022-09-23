import sys

sys.stdin = open('input.txt')


def chk(d_x, d_y, t):
    while True:
        d_x, d_y = d_x + dx[t], d_y + dy[t]
        if d_x in success or d_y in success or board[d_x][d_y] == 0:
            return False
        if board[d_x][d_y] == s:
            return True


# 상 하 좌 우 좌상 우상 좌하 우하
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    success = (-1, n)
    b = 1
    w = 2
    for i in range(n // 2 - 1, n // 2 + 1):
        for j in range(n // 2 - 1, n // 2 + 1, 2):
            board[i][j] = w
            board[i][j + 1] = b
        w = w % 2 + 1
        b = b % 2 + 1
    for _ in range(m):
        x, y, s = map(int, input().split())
        i, j = x - 1, y - 1
        board[i][j] = s
        for d in range(8):
            di, dj = i + dx[d], j + dy[d]
            if di not in success and dj not in success and board[di][dj] == s % 2 + 1:
                if chk(di, dj, d):
                    board[di][dj] = s
                    while True:
                        di, dj = di + dx[d], dj + dy[d]
                        if board[di][dj] == s:
                            break
                        board[di][dj] = s
    answer = 0
    for b in board:
        answer += b.count(2)
    print(m + 4 - answer, answer)