from heapq import heappop, heappush
import sys

input = sys.stdin.readline


def sol():
    def dijkstra(start):
        distance[start] = 0
        heap = [(0, start)]
        while heap:
            min_dis, min_node = heappop(heap)
            if min_dis > distance[min_node]:
                continue
            for next_dis, next_node in board[min_node]:
                new_dis = next_dis + min_dis
                if new_dis < distance[next_node]:
                    distance[next_node] = new_dis
                    heappush(heap, (new_dis, next_node))
        return

    v, e = map(int, input().split())
    s = int(input())
    board = [[] for _ in range(v + 1)]
    INF = 999999999
    distance = [INF] * (v + 1)
    for _ in range(e):
        u, v, w = map(int, input().split())
        board[u].append((w, v))
    dijkstra(s)
    for num in distance[1:]:
        if num == INF:
            print("INF")
        else:
            print(num)


sol()
