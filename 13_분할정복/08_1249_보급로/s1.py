from heapq import heappush, heappop
import sys

sys.stdin = open('input.txt')


def sol():
    def dijkstra(s_x, s_y):
        distance[s_x][s_y] = 0
        heap = [(0, s_x, s_y)]
        while heap:
            min_dis, min_x, min_y = heappop(heap)
            if min_dis > distance[min_x][min_y]:
                continue
            for d in range(4):
                n_x, n_y = min_x + dx[d], min_y + dy[d]
                if 0 <= n_x < n and 0 <= n_y < n:
                    new_dis = min_dis + board[n_x][n_y]
                    if new_dis < distance[n_x][n_y]:
                        distance[n_x][n_y] = new_dis
                        heappush(heap, (new_dis, n_x, n_y))
        return

    n = int(input())
    board = [list(map(int, list(input()))) for _ in range(n)]
    INF = 9999999
    distance = [[INF] * n for _ in range(n)]
    dijkstra(0, 0)
    print(distance[n - 1][n - 1])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
