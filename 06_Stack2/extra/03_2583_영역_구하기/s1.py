import sys
sys.setrecursionlimit(10**6)

# board판을 검사하면서 0이면 legion_cnt += 1을 하고 현재 위치를 1로 바꾸는 함수
def find_region(x, y):
    global legion_cnt
    board[x][y] = 1
    legion_cnt += 1
    for n in range(4):
        nx, ny = x + dx[n], y + dy[n]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            find_region(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
M, N, K = map(int, input().split())
# board 세팅
board = [[0] * M for _ in range(N)]
# 받은 좌표의 영역을 board에 1로 색칠
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1
# 지역의 개수를 세는 result_cnt와 지역의 크기를 오름차순으로 정렬할 빈 logion list 세팅
result_cnt = 0
legion = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            # 영역을 찾으면 result_cnt += 1
            result_cnt += 1
            # 영역의 크기를 셀 legion_cnt 세팅
            legion_cnt = 0
            find_region(i, j)
            # 영역의 크기를 legion에 추가
            legion.append(legion_cnt)

print(result_cnt)
print(*sorted(legion))
