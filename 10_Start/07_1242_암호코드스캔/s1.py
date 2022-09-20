import sys

sys.stdin = open('input.txt')


def chk_true(num, remove):
    board_num = sum(num[1:])
    n = 0
    while True:
        n += 1
        if board_num < 56 * n:
            break
    ck = ""
    for i in range(0, len(num), 4):
        ct = num[i:i + 4]
        for k in range(1, 4):
            ck += str(ct[k] // n)
    if ck in remove:
        return 0
    num_10 = []
    for i in range(0, 24, 3):
        num_10.append(chk_num.index(ck[i:i + 3]))
    result = 0
    for j in range(len(num_10)):
        if j % 2:
            result += int(num_10[j])
        else:
            result += int(num_10[j]) * 3
    if result % 10:
        return 0
    remove.add(ck)
    return sum(num_10)


def sol():
    h, length = map(int, input().split())
    chk = "0" * length
    board = [chk] + [input()[:length] for _ in range(h)]
    answer = set()
    remove = set()
    for i in range(1, h + 1):
        if board[i] != chk and board[i] != board[i - 1]:
            chk_board = bin(int(board[i], 16))[2:].rstrip("0")
            cnt = 0
            num = 1
            a = [0]
            for p in range(len(chk_board)):
                if int(chk_board[p]) == num:
                    cnt += 1
                else:
                    a.append(cnt)
                    num = abs(num - 1)
                    cnt = 1
            a.append(cnt)
            for j in range(0, len(a), 32):
                answer.add(tuple(a[j:j + 32]))
    result = 0
    for chk_answer in tuple(answer):
        result += chk_true(chk_answer, remove)
    print(result)


chk_num = ('211', '221', '122', '411', '132', '231', '114', '312', '213', '112')
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
