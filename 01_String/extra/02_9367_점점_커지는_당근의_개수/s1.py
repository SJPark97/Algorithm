import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    # N 값, 수확하는 당근의 크기 받아오기
    N = int(input())
    C = list(map(int, input().split()))

    # 연속으로 커지는 개수 설정
    high_cnt = 1
    cnt = 1

    for case in range(N-1):
        if C[case] < C[case+1]:
            cnt += 1
            if cnt > high_cnt:
                high_cnt = cnt
        else:
            cnt = 1
    print(high_cnt)

