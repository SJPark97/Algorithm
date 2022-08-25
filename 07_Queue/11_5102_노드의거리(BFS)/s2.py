import sys
sys.stdin = open("input.txt")


def bfs(qu, g, cnt):
    global result
    queue1 = []
    if result != 0:
        return

    while qu:
        start = qu.pop(0)
        for node in board[start]:
            if node == g:
                result = cnt
                return
            elif not visit[node]:
                visit[node] = True
                queue1.append(node)
    if queue1:
        bfs(queue1, g, cnt+1)
    return


T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    V, E = map(int, input().split())
    board = [[] for _ in range(V+1)]
    visit = [False] * (V+1)

    for _ in range(E):
        v1, v2 = map(int, input().split())
        board[v1].append(v2)
        board[v2].append(v1)
    S, G = map(int, input().split())
    queue = [S]
    visit[S] = True
    result = 0
    bfs(queue, G, 1)
    print(result)
