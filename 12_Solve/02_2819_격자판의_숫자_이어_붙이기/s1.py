import sys

sys.stdin = open('input.txt')


def dfs(x, y, t):
    if t == 7:
        answer.add(tuple(result))
        return
    for n in range(4):
        nx, ny = x + dx[n], y + dy[n]
        if nx not in success and ny not in success:
            result.append(board[nx][ny])
            dfs(nx, ny, t + 1)
            result.pop()


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
success = (-1, 4)
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    board = [tuple(map(int, input().split())) for _ in range(4)]
    answer = set()
    for i in range(4):
        for j in range(4):
            result = [board[i][j]]
            dfs(i, j, 1)
    print(len(answer))
