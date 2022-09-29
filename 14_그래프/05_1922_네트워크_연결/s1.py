import sys

input = sys.stdin.readline


def sol():
    def find_set(node):
        if node != parent[node]:
            parent[node] = find_set(parent[node])
        return parent[node]

    n = int(input())
    m = int(input())
    board = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[2])
    parent = list(range(n + 1))
    line = 0
    answer = 0
    for x, y, cost in board:
        x_root, y_root = find_set(x), find_set(y)

        if x_root != y_root:
            line += 1
            answer += cost
            if line >= n - 1:
                print(answer)
                return
            parent[x_root] = y_root


sol()