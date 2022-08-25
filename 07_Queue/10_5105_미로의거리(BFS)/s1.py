import sys
sys.stdin = open("input.txt")


def find_index(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 3:
                location = (i, j)
                return location


def bfs(location):
    x = location[0]
    y = location[1]
    queue = [location]
    visit[x][y] = True
    total = 0
    while total < N*N:
        queue1 = []
        while queue:
            x, y = queue.pop(0)
            for n in range(4):
                mx, my = x + dx[n], y + dy[n]
                if 0 <= mx < N and 0 <= my < N and not visit[mx][my]:
                    if board[mx][my] == 0:
                        visit[mx][my] = True
                        queue1.append((mx, my))
                    elif board[mx][my] == 2:
                        return total
        queue = queue1.copy()
        total += 1
    return 0


T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    visit = [[False] * N for _ in range(N)]
    print(bfs(find_index(board)))

