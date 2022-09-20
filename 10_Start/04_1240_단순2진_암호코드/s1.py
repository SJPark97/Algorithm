import sys

sys.stdin = open('input.txt')


def chk_true(answer):
    result = 0
    for num in range(8):
        if num % 2:
            result += answer[num]
        else:
            result += answer[num] * 3
    if result % 10:
        return False
    return True


def sol():
    h, length = map(int, input().split())
    board = [input() for _ in range(h)]
    answer = []
    for i in range(h):
        if int(board[i], 2):
            chk_board = board[i]
            break
    for j in range(length - 1, -1, -1):
        if chk_board[j] == '1':
            chk_board = chk_board[j - 55:j + 1]
            break
    for x in range(0, 56, 7):
        answer.append(chk.index(chk_board[x:x + 7]))
    if chk_true(answer):
        print(sum(answer))
        return
    print(0)
    return


chk = ('0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011')
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
