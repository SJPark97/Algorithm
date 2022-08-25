import sys

sys.stdin = open("input.txt")

# 단순하게 반복횟수를 나눈 나머지를 이용
T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')
    N, M = map(int, input().split())

    num_list = list(map(int, input().split()))

    print(num_list[M % N])

# queue를 이용
T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')
    N, M = map(int, input().split())

    num_list = list(map(int, input().split()))

    for _ in range(M):
        num_list.append(num_list.pop(0))

    print(num_list[0])
