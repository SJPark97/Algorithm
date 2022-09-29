from heapq import heappop, heappush


def sol():
    def dijkstra(start):
        distance[start] = 0
        heap = [(0, start)]
        while heap:
            min_dis, min_node = heappop(heap)
            if min_dis <= distance[min_node]:
                for dis, next_node in board[min_node]:
                    new_dis = min_dis + dis
                    if new_dis < distance[next_node]:
                        distance[next_node] = new_dis
                        heappush(heap, (new_dis, next_node))

    n, e = map(int, input().split())
    board = [[] for _ in range(n + 1)]
    INF = 9999999999
    distance = [INF] * (n + 1)
    for _ in range(e):
        s, e, w = map(int, input().split())
        board[s].append((w, e))
    dijkstra(0)
    print(distance[n])


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
