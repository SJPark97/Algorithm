import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}')

    N = int(input())
    first_list = [list(map(int, input().split())) for _ in range(N)]
    #  270도 회전
    final_list = list(zip(*first_list))[::-1]
    #  180도 회전
    thd_list = list(zip(*final_list))[::-1]
    #  90도 회전
    sec_list = list(zip(*thd_list))[::-1]

    for i in range(N):
        print(*sec_list[i], sep='', end=' ')
        print(*thd_list[i], sep='', end=' ')
        print(*final_list[i], sep='', end=' ')
        print()
