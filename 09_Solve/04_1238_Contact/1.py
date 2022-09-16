import sys

sys.stdin = open('input.txt')


def bfs(s, visited, graph):
    visited[s] = True
    queue = [s, 0]
    result = [(0, 0)]  # result = depth, idx(next_v)

    while queue:
        x, d = queue.pop(0)

        for next_v in graph[x]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v, d + 1)
                if result[0][0] > queue[-1][1] - 1:  # d를 비교해서 높으면 바꿔주기
                    result[0][0] = d
                    result[0][1] = next_v
    return result[0][1]


def sol(v, s):
    visited = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]
    # 그래프 채워넣기
    for n in range(0, v, 2):
        val_1, val_2 = data[n], data[n+1]
        graph[val_1].append(val_2)
    return bfs(s, visited, graph)


for case in range(1, 11):
    v, s = map(int, input().split())  # v = 정점의 수, s = 시작점
    data = list(map(int, input().split()))
    result = []
    print(f'{case} {sol(v, s)}')