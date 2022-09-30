import sys

input = sys.stdin.readline


def sol():
    def find_set(node):
        if node != parent[node]:
            parent[node] = find_set(parent[node])
        return parent[node]

    n, m = map(int, input().split())
    board = []
    parent = list(range(n + 1))
    answer = []
    line = 0
    for _ in range(m):
        a, b, c = list(map(int, input().split()))
        board.append((c, a, b))
    board.sort()
    for cost, x, y in board:
        x_root, y_root = find_set(x), find_set(y)
        if x_root != y_root:
            parent[x_root] = y_root
            answer.append(cost)
            line += 1
            if line >= n - 1:
                break
    answer.sort()
    print(sum(answer[:-1]))


sol()
