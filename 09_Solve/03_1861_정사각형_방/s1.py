import sys
sys.setrecursionlimit(2500*1000)
sys.stdin = open('input.txt')


def chk(x, y):
    visit[x][y] = True
    visit_room.append(room[x][y])
    for n in range(4):
        nx, ny = x + dx[n], y + dy[n]
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and abs(room[nx][ny] - room[x][y]) == 1:
            chk(nx, ny)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False] * N for _ in range(N)]
    result = [0, 0]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                visit_room = []
                chk(i, j)
                if result[1] < len(visit_room) or result[1] == len(visit_room) and result[0] > min(visit_room):
                    result = [min(visit_room), len(visit_room)]
    print(*result)
