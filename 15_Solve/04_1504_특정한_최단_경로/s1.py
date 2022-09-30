from heapq import heappop, heappush
import sys

input = sys.stdin.readline


def sol():
    def dijkstra(start):
        distance = [INF] * (n + 1)
        distance[start] = 0
        heap = [(0, start)]
        while heap:
            min_dis, min_node = heappop(heap)
            if min_dis > distance[min_node]:
                continue
            for next_dis, next_node in board[min_node]:
                new_dis = min_dis + next_dis
                if new_dis < distance[next_node]:
                    distance[next_node] = new_dis
                    heappush(heap, (new_dis, next_node))
        return distance

    n, e = map(int, input().split())
    board = [[] for _ in range(n + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        board[a].append((c, b))
        board[b].append((c, a))
    must_pass = tuple(map(int, input().split()))  # 탐색 시작지점
    INF = 100 ** 10
    result = []
    for s in must_pass:
        result.append(dijkstra(s))
    way1 = result[0][1] + result[0][must_pass[1]] + result[1][n]
    way2 = result[1][1] + result[1][must_pass[0]] + result[0][n]
    if min(way1, way2) >= INF:
        print(-1)
        return
    print(min(way1, way2))


sol()
