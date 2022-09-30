import sys

sys.stdin = open('input.txt')


def sol():
    n = int(input())
    board_x = tuple(map(int, input().split()))
    board_y = tuple(map(int, input().split()))
    e = float(input())
    watter_road = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            watter_road[i].append((((board_x[i] - board_x[j]) ** 2 + (board_y[i] - board_y[j]) ** 2), j))
            watter_road[j].append((((board_x[i] - board_x[j]) ** 2 + (board_y[i] - board_y[j]) ** 2), i))
    INF = 100**10
    visit = [False] * n
    distance = [INF] * n
    distance[0] = 0
    answer = 0
    for _ in range(n):
        min_dis = INF
        for i, dis in enumerate(distance):
            if not visit[i] and dis < min_dis:
                min_node = i
                min_dis = dis
        visit[min_node] = True
        answer += min_dis
        for next_dis, next_node in watter_road[min_node]:
            if not visit[next_node] and next_dis < distance[next_node]:
                distance[next_node] = next_dis
    print(round(answer * e))


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
