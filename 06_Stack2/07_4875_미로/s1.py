import sys

sys.stdin = open("input.txt")


def find_wayout(x, y):
    global signal
    # 방문지역 표시
    visit[x][y] = True
    for n in range(4):
        nx, ny = x + dx[n], y + dy[n]
        if 0 <= nx < N and 0 <= ny < N:
            # 만약 앞에 '2'가 있으면 signal에 1을 저장
            if board[nx][ny] == '2':
                signal = 1
                return
            # 방문하지 않고 앞이 '0'이면 dfs 계속 수행
            elif board[nx][ny] == '0' and not visit[nx][ny]:
                find_wayout(nx, ny)



T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    N = int(input())

    board = [input() for _ in range(N)]
    visit = [[False] * N for _ in range(N)]
    signal = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == '3':
                find_wayout(i, j)
                # 찾았으니 반복문 더 반복하지 않고 종료
                break
    print(signal)
