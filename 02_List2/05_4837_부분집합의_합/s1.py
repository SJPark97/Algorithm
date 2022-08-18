import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    # N, K 값 입력
    N, K = map(int, input().split())

    # 집합 A
    A = list(range(1, 13))

    # 결과값
    count = 0

    # 부분집합의 길이가 N인 부분집합 찾기
    for i in range(1 << 12):

        # 부분집합 리스트
        N_number = []

        for j in range(12):
            if i & (1 << j):
                N_number.append(A[j])

        # 부분집합의 길이가 N이고 합이 K이면 count += 1
        if len(N_number) == N and sum(N_number) == K:
            count += 1

    print(count)
