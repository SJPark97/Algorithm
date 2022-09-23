import sys

sys.stdin = open('input.txt')


def cnt(x, y, d):
    cnt_home = 0
    for home in homes_list:
        if abs(home[0] - x) + abs(home[1] - y) <= d:
            cnt_home += 1
    return cnt_home


def chk(k):
    answer = []
    if k == 0:
        return
    cost = k * k + (k - 1) * (k - 1)
    for a in range(n):
        for b in range(n):
            home = cnt(a, b, k-1)
            if home * m >= cost:
                answer.append(home)
    if answer:
        print(max(answer))
        return
    chk(k - 1)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    n, m = map(int, input().split())
    homes = [list(map(int, input().split())) for _ in range(n)]
    homes_num = sum(map(sum, homes))
    homes_list = []
    max_k = int(((homes_num * m - 2) / 2) ** 0.5 + 0.5)
    if max_k >= n:
        print(homes_num)
        continue
    for i in range(n):
        for j in range(n):
            if homes[i][j] == 1:
                homes_list.append((i, j))
    chk(max_k)

