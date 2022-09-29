from heapq import heappush, heappop
import sys

input = sys.stdin.readline


def sol():
    def dijkstra(distance, board, start):
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

    n, m, x = map(int, input().split())
    board1 = [[] for _ in range(n + 1)]
    board2 = [[] for _ in range(n + 1)]
    INF = 99999999
    distance1 = [INF] * (n + 1)
    distance2 = [INF] * (n + 1)
    for _ in range(m):
        s, e, w = map(int, input().split())
        board1[s].append((w, e))
        board2[e].append((w, s))
    dijkstra(distance1, board1, x)
    dijkstra(distance2, board2, x)
    answer = 0
    for i in range(1, n + 1):
        answer = max(answer, distance1[i] + distance2[i])
    print(answer)


sol()
