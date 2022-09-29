def sol():
    def find_set(node):
        if node != parent[node]:
            parent[node] = find_set(parent[node])
        return parent[node]

    n = int(input())
    m = int(input())
    parent = list(range(n + 1))
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(n):
            if line[j] == 1:
                i_root, j_root = find_set(i + 1), find_set(j + 1)
                if i_root != j_root:
                    if i_root < j_root:
                        parent[i_root] = j_root
                    else:
                        parent[j_root] = i_root
    path = list(map(int, input().split()))
    root = find_set(path[0])
    for i in range(1, m):
        if root != find_set(path[i]):
            print("NO")
            return
    print("YES")
    return


sol()
