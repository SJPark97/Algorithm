from heapq import heappush, heappop


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

    n, m, k = map(int, input().split())
    board = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, w = map(int, input().split())
        board[s].append((w, e))
    INF = 10 ** 10
    result = [[]]
    for s in range(1, n + 1):
        result.append(dijkstra(s))
    print(*result, sep="\n")
    answer = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(n + 1):
            if i == 1:
                answer[j].append(result[i][j])
            elif i != j:
                answer[j].append(result[1][i] + result[i][j])
    print()
    print(*answer, sep="\n")
    return


sol()
