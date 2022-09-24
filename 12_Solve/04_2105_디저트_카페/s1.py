import sys

sys.stdin = open('input.txt')


def list_append(x, y, t_d, t_u, d, dessert_list):
    for _ in range(t_u):
        x, y = x + dx[d], y + dy[d]
        if 0 <= x < n and 0 <= y < n:
            dessert_list.append(board[x][y])
        else:
            return False
    for _ in range(t_d):
        x, y = x + dx[(d + 1) % 2], y + dy[(d + 1) % 2]
        if 0 <= x < n and 0 <= y < n:
            dessert_list.append(board[x][y])
        else:
            return False
    return True


def chk(x, y, d):
    while d > 1:
        for up_down in range(1, d):
            left_right = d - up_down
            dessert_list = [board[x][y]]
            if list_append(x, y, up_down, left_right, 0, dessert_list):
                if list_append(x, y, left_right, up_down, 1, dessert_list):
                    if len(set(dessert_list)) == d * 2:
                        return d
        d -= 1
    return -1


dx = [1, 1]
dy = [-1, 1]
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=' ')
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = -0.5
    for i in range(n - 2):
        for j in range(1, n - 1):
            result = chk(i, j, n - i - 1)
            if answer < result:
                answer = result
        if n - 1 - i <= answer:
            break
    print(int(answer * 2))
