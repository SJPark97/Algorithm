def counting(x, y):
    visit_list[x][y] = True
    global home_total
    home_total += 1
    for m in range(4):
        m_x = x + dx[m]
        m_y = y + dy[m]
        if 0 <= m_x < N and 0 <= m_y < N and home_list[m_x][m_y] and not visit_list[m_x][m_y]:
            counting(m_x, m_y)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
home_list = [list(map(int, input())) for _ in range(N)]
visit_list = [[False]*N for _ in range(N)]
finish_cnt = []

for i in range(N):
    for j in range(N):
        if home_list[i][j] and not visit_list[i][j]:
            home_total = 0
            counting(i, j)
            finish_cnt.append(home_total)

print(len(finish_cnt))
for num in sorted(finish_cnt):
    print(num)