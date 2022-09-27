import sys

sys.stdin = open('input.txt')


def sol():
    def dfs(start, time):
        nonlocal cnt
        if time >= cnt:
            return
        charge = board[start]
        for i in range(charge, 0, -1):
            if start+i < n:
                dfs(start+i, time + 1)
            elif cnt > time:
                cnt = time
        return

    board = list(map(int, input().split()))
    n = board[0]
    cnt = n
    dfs(1, 0)
    print(cnt)


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
