import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    # N 받아오기, 문제 받아오기, 결과값, 최고값 설정
    N = int(input())
    number = input()
    cnt_result = 0
    cnt = 0

    for test in number:
        if test == '0':
            cnt = 0
        else:
            cnt += 1
        if cnt > cnt_result:
            cnt_result = cnt

    print(cnt_result)
