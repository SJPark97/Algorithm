import sys
sys.stdin = open("input.txt")


def bfs(s, g):
    queue = [s]
    visit[s] = True
    total = 0
    while total < E:
        queue1 = []
        total += 1
        while queue:
            start = queue.pop(0)
            for node in board[start]:
                if node == g:
                    return total
                elif not visit[node]:
                    queue1.append(node)
                    visit[node] = True
        queue = queue1.copy()
    return 0


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

    print(bfs(S, G))
