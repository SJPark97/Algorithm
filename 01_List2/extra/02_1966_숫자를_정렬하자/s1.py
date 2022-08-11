import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    # N 받아오기
    N = int(input())

    num_list = sorted(list(map(int, input().split())))

    print(*num_list)