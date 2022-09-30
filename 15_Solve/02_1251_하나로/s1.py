import sys

sys.stdin = open('input.txt')


def sol():
    def find_set(node):
        if node != parent[node]:
            parent[node] = find_set(parent[node])
        return parent[node]

    n = int(input())
    board_x = tuple(map(int, input().split()))
    board_y = tuple(map(int, input().split()))
    watter_road = []
    for i in range(n):
        for j in range(i + 1, n):
            watter_road.append(
                (((board_x[i] - board_x[j]) ** 2 + (board_y[i] - board_y[j]) ** 2), i, j))
    watter_road.sort()
    e = float(input())
    parent = list(range(n))
    answer = 0
    line = 0
    for path, x, y in watter_road:
        x_root, y_root = find_set(x), find_set(y)
        if x_root != y_root:
            line += 1
            answer += path
            parent[x_root] = y_root
            if line >= n - 1:
                break
    print(round(answer * e))


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
