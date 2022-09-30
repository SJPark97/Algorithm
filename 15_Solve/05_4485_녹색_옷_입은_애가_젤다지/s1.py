from heapq import heappush, heappop
import sys

input = sys.stdin.readline


def sol():
    def dijkstra(s_x, s_y):
        distance[s_x][s_y] = board[s_x][s_y]
        heap = [(board[s_x][s_y], s_x, s_y)]
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
        return distance[n - 1][n - 1]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    tc = 1
    while True:
        n = int(input())
        if n == 0:
            break
        board = [list(map(int, input().split())) for _ in range(n)]
        INF = 9999999
        distance = [[INF] * n for _ in range(n)]
        dijkstra(0, 0)
        print(f'Problem {tc}: {distance[n - 1][n - 1]}')
        tc += 1


sol()
