import sys

sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}', end = ' ')
    N = int(input())
    num_list = list(map(int, input().split()))
    for i in range(N-1, 0, -1): #버블정렬
        for j in range(0, i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    result = num_list[-1] - num_list[0] #제일 큰 수와 작은 수 빼기
    print(result)
