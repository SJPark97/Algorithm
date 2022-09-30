from heapq import heappush, heappop
import sys

# input = sys.stdin.readline
sys.stdin = open("input.txt")


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
    result = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        s, e, w = map(int, input().split())
        board[s].append((w, e))
        result[s][e].append(w)
    INF = 10 ** 10
    for s in range(1, n + 1):
        i = 0
        for num in dijkstra(s):
            result[s][i].append(num)
            i += 1
    answer = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(n + 1):
            if i == 1:
                answer[j].extend(result[i][j])
            elif i != j:
                for num1 in set(result[1][i]):
                    for num2 in set(result[i][j]):
                        answer[j].append(num1 + num2)
    for i in range(1, n + 1):
        ans = sorted(list(set(answer[i])))
        print(ans)
        if len(ans) < k or ans[k - 1] >= INF:
            print(-1)
        else:
            print(ans[k - 1])
    return


sol()
