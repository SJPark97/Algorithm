import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt")

# 정상 사람의 영역 검증 함수
def normal(x, y):
    visit[x][y] = True
    for n in range(4):
        nx, ny = x + dx[n], y + dy[n]
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and board[nx][ny] == color:
            normal(nx, ny)

# 적록색약 사람의 영역 검증 함수
def blindness(x, y):
    blindness_visit[x][y] = True
    for n in range(4):
        nx, ny = x + dx[n], y + dy[n]
        # 색이 빨간색이나 초록색이면 같이 검사
        if color in 'GR':
            if 0 <= nx < N and 0 <= ny < N and not blindness_visit[nx][ny] and board[nx][ny] in 'GR':
                blindness(nx, ny)
        else:
            if 0 <= nx < N and 0 <= ny < N and not blindness_visit[nx][ny] and board[nx][ny] == color:
                blindness(nx, ny)


N = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = [input() for _ in range(N)]
visit = [[False]*N for _ in range(N)]
blindness_visit = [[False]*N for _ in range(N)]
normal_region = 0
blindness_region = 0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            normal_region += 1
            color = board[i][j]
            normal(i, j)
        if not blindness_visit[i][j]:
            blindness_region += 1
            color = board[i][j]
            blindness(i, j)


print(normal_region, blindness_region)
