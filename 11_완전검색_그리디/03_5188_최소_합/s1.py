def dfs(x, y):
    global answer, result
    if result >= answer:
        return
    if x == l-1 and y == l-1 and answer > result:
        answer = result
        return
    for n in range(2):
        nx, ny = x + dx[n], y + dy[n]
        if 0 <= nx < l and 0 <= ny < l and not visit[nx][ny]:
            visit[nx][ny] = True
            result += board[nx][ny]
            dfs(nx, ny)
            visit[nx][ny] = False
            result -= board[nx][ny]


dx = [1, 0]
dy = [0, 1]
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=' ')
    l = int(input())
    board = [list(map(int, input().split())) for _ in range(l)]
    visit = [[False] * l for _ in range(l)]
    visit[0][0] = True
    answer = 9 * (l**2)
    result = board[0][0]
    dfs(0, 0)
    print(answer)
