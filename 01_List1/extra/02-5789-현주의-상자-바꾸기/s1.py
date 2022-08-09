import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    print(f'#{test_case}', end = ' ')

    # N, Q 값 입력, 결과 list 만들기
    N, Q = map(int, input().split())
    result = [0] * N

    # i 값을 list에 넣기
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for num in range(L - 1, R):
            result[num] = i

    print(*result)
