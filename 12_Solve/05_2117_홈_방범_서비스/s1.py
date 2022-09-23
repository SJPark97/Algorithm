from collections import deque
import sys

sys.stdin = open('input.txt')


def bfs(s_x, s_y):
    visit = [[False] * n for _ in range(n)]
    visit[s_x][s_y] = True
    queue = deque([(s_x, s_y, 0)])
    cnt = 0
    chk_k = 2
    chk = []
    while queue:
        x, y, t = queue.popleft()
        # print(cnt, t)
        if t == chk_k:
            chk.append((cnt, cnt * m - (t * t + (t - 1) * (t - 1))))
            chk_k += 1
        if homes[x][y] == 1:
            cnt += 1
        if t == max_k:
            continue
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx, ny, t + 1))
    return chk


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    n, m = map(int, input().split())
    homes = [list(map(int, input().split())) for _ in range(n)]
    homes_num = sum(map(sum, homes))
    max_k = int(((homes_num * m - 2) / 2) ** 0.5 + 0.5)
    result = 1
    if max_k >= n:
        print(homes_num)
        continue
    for i in range(n):
        for j in range(n):
            for cost in bfs(i, j):
                if cost[1] >= 0 and result < cost[0]:
                    result = cost[0]
    print(result)

