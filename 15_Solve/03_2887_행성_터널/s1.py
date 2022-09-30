import sys

input = sys.stdin.readline


def sol():
    def find_set(node):
        if node != parent[node]:
            parent[node] = find_set(parent[node])
        return parent[node]

    n = int(input())
    location = [list(map(int, input().split())) + [i] for i in range(n)]
    planet_road = []
    for j in range(3):
        location.sort(key=lambda x: x[j])
        for i in range(1, n):
            planet_road.append((abs(location[i - 1][j] - location[i][j]), location[i - 1][3], location[i][3]))
    planet_road.sort()
    parent = list(range(n))
    answer = 0
    road = 0
    for cost, x, y in planet_road:
        x_root, y_root = find_set(x), find_set(y)
        if x_root != y_root:
            parent[x_root] = y_root
            answer += cost
            road += 1
            if road >= n - 1:
                break

    print(answer)


sol()
