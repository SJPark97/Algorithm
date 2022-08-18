import sys

sys.stdin = open("input.txt")

def dfs(n):
    visit[n] = True
    for v in graph[n]:
        if not visit[v]:
            dfs(v)

for _ in range(1, 11):

    test_case, case_num = map(int, input().split())
    print(f'#{test_case}', end=' ')

    road = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    visit = [False] * (100)

    for start in range(case_num):
        graph[road[start*2]].append(road[start*2+1])

    result = 0
    dfs(0)
    if visit[99]:
        result = 1

    print(result)
