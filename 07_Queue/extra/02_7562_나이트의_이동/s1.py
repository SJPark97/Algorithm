from collections import deque
import sys
sys.stdin = open("input.txt")


def check(now, future):
    i, j = now[0], now[1]
    f_i, f_j = future[0], future[1]
    nights_visit[i][j] = True
    queue = deque([(i, j, 1)])
    while queue:
        x, y, t = queue.popleft()
        for n in range(8):
            mx, my = x + dx[n], y + dy[n]
            if 0 <= mx < I and 0 <= my < I and not nights_visit[mx][my]:
                if mx == f_i and my == f_j:
                    return t
                else:
                    nights_visit[mx][my] = True
                    queue.append((mx, my, t+1))
    return 0


dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

T = int(input())
for _ in range(T):

    I = int(input())
    nights_visit = [[False]*I for _ in range(I)]
    nights_now = list(map(int, input().split()))
    nights_future = list(map(int, input().split()))
    print(check(nights_now, nights_future))

