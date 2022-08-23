import sys

sys.stdin = open("input.txt")

# x : 시작위치 board[x], board_sum : 단계별 합계
def board_visit(x, board_sum):
    global total
    # board_sum이 total보다 높아지면 종료 (백트래킹)
    if board_sum >= total:
        return
    # 길이의 끝까지 도달했을때 조건 비교
    if x == N and board_sum < total:
        total = board_sum
    # dfs
    else:
        for i in range(N):
            if not visit[i]:
                visit[i] = True
                board_visit(x + 1, board_sum + board[x][i])
                visit[i] = False


T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [False] * N
    # total에 board에 있는 모든 값의 합을 넣어서 클 수밖에 없게 만들기
    total = sum(map(sum, board))
    board_visit(0, 0)
    print(total)
