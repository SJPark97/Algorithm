import sys

sys.stdin = open("input.txt")


def dfs(n):
    visit[n] = True
    for v in graph[n]:
        if not visit[v]:
            dfs(v)


T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visit = [False] * (V+1)

    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)

    S, G = map(int, input().split())
    result = 0
    dfs(S)
    if visit[G]:
        result = 1
    print(result)

