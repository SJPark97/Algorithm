from heapq import heappush, heappop
import sys

input = sys.stdin.readline


def sol():
    def dijkstra(start):
        distance[start][0] = 0
        heap = [(0, start)]
        while heap:
            min_dis, min_node = heappop(heap)
            if min_dis > distance[min_node][-1]:
                continue
            for next_dis, next_node in board[min_node]:
                new_dis = min_dis + next_dis
                if new_dis < distance[next_node][-1]:
                    distance[next_node][-1] = new_dis
                    distance[next_node].sort()
                    heappush(heap, (new_dis, next_node))
        return

    n, m, k = map(int, input().split())
    board = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, w = map(int, input().split())
        board[s].append((w, e))
    INF = 10 ** 10
    distance = [[INF] * k for _ in range(n + 1)]
    dijkstra(1)
    for i in range(1, n + 1):
        if distance[i][k - 1] >= INF:
            print(-1)
        else:
            print(distance[i][k - 1])


sol()
