from heapq import heappop, heappush


def sol():
    def dijkstra(start_x, start_y):
        distance[start_x][start_y] = 0
        heap = [(0, start_x, start_y, board[start_x][start_y])]
        while heap:
            min_dis, min_x, min_y, min_col = heappop(heap)
            if min_dis > distance[min_x][min_y]:
                continue
            for d in range(4):
                next_x, next_y = min_x + dx[d], min_y + dy[d]
                if 0 <= next_x < n and 0 <= next_y < n:
                    up = 0
                    if board[next_x][next_y] > min_col:
                        up = board[next_x][next_y] - min_col
                    new_dis = min_dis + up + 1
                    if new_dis < distance[next_x][next_y]:
                        distance[next_x][next_y] = new_dis
                        heappush(heap, (new_dis, next_x, next_y, board[next_x][next_y]))
        return

    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    INF = 999999999999
    distance = [[INF] * n for _ in range(n)]
    dijkstra(0, 0)
    print(distance[n - 1][n - 1])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
