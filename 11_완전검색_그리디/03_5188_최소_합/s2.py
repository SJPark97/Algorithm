for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=' ')
    l = int(input())
    board = [list(map(int, input().split())) for _ in range(l)]
    for i in range(1, l):
        board[0][i] += board[0][i - 1]
        board[i][0] += board[i - 1][0]
    for i in range(1, l):
        for j in range(1, l):
            board[i][j] += min(board[i - 1][j], board[i][j - 1])
    print(board[l-1][l-1])
