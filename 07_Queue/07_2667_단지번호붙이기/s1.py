def bfs(x, y):
    queue = [(x, y)]
    visit_list[x][y] = True
    total = 1

    while queue:
        x, y = queue.pop(0)
        for n in range(4):
            mx, my = x + dx[n], y + dy[n]
            if 0 <= mx < N and 0 <= my < N and not visit_list[mx][my] and home_list[mx][my] == 1:
                visit_list[mx][my] = True
                queue.append((mx, my))
                total += 1
    return total


N = int(input())
home_list = [list(map(int, input())) for _ in range(N)]
visit_list = [[False]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []

for i in range(N):
    for j in range(N):
        if home_list[i][j] == 1 and not visit_list[i][j]:
            result.append(bfs(i, j))

print(len(result))
for cnt in sorted((result)):
    print(cnt)
