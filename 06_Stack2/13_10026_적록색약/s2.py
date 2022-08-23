import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt")


# 영역 검증 함수
def check(x, y, visit):
    visit[x][y] = True
    for n in range(4):
        nx, ny = x + dx[n], y + dy[n]
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and board[nx][ny] in color:
            check(nx, ny, visit)


N = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = [input() for _ in range(N)]
normal_visit = [[False]*N for _ in range(N)]
blindness_visit = [[False]*N for _ in range(N)]
normal_region = 0
blindness_region = 0
for i in range(N):
    for j in range(N):
        if not normal_visit[i][j]:
            normal_region += 1
            color = board[i][j]
            check(i, j, normal_visit)
        if not blindness_visit[i][j]:
            blindness_region += 1
            if board[i][j] in 'RG':
                color = 'RG'
            else:
                color = board[i][j]
            check(i, j, blindness_visit)

print(normal_region, blindness_region)
