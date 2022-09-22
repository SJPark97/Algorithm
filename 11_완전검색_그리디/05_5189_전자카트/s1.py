from itertools import permutations

for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    chk = list(permutations(list(range(2, n + 1)), n - 1))
    start = 1
    answer = sum(map(sum, board))
    for c in chk:
        result = 0
        for end in list(c) + [1]:
            result += board[start-1][end-1]
            start = end
        if answer > result:
            answer = result
    print(answer)