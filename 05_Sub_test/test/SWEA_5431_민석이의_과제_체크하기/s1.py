import sys

sys.stdin = open("input1.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    n, k = map(int, input().split())
    k_list = list(map(int, input().split()))
    for n_list in range(1, n + 1):
        if n_list not in k_list:
            print(n_list, end=' ')
    print()


