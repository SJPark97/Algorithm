import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    # N, K 받아오기
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]

