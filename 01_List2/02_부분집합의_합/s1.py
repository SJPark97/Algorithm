import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')

    # 값을 받아 list에 입력
    arr = list(map(int, input().split()))
    n = len(arr)

    # 결과값 (0, 1)
    result = 0
    for i in range(1, 1 << n):   # 2^n 부분 집합의 개수
        check = 0
        for j in range(n):  # list의 길이만큼 비트를 비교
            if i & (1 << j):  # i의 j번 비트가 1인경우
                check += arr[j]
        if check == 0:
            result = 1
            break

    print(result)
