import sys

sys.stdin = open('input.txt')


def sol():
    num = float(input())
    answer = ""
    cnt = 0
    while num and cnt < 13:
        cnt += 1
        num *= 2
        if num >= 1:
            answer += "1"
            num -= 1
        else:
            answer += "0"
    if cnt == 13:
        print("overflow")
        return
    print(answer)
    return


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
