def sol():
    def find_set(node):
        if node != parent[node]:
            parent[node] = find_set(parent[node])
        return parent[node]

    v, e = map(int, input().split())
    board = sorted([list(map(int, input().split())) for _ in range(e)], key=lambda x: x[2])
    parent = list(range(v + 1))
    line = 0
    answer = 0
    for x, y, w in board:
        x_root, y_root = find_set(x), find_set(y)

        if x_root != y_root:
            parent[x_root] = y_root
            line += 1
            answer += w
            if line >= v:
                print(answer)
                return


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()