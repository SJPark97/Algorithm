import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    # N, M, 사진 받아오기
    N, M = map(int, input().split())
    map_picture = [list(map(int, input().split())) for _ in range(N)]

    # 최고길이 설정
    highest_len = 0

    # 가로줄
    for i in range(N):

        # 길이 초기값 설정
        row_len = 0
        for j in range(M):
            if map_picture[i][j]:
                row_len += 1
                if highest_len < row_len:
                    highest_len = row_len
            else:
                row_len = 0
                
    # 세로줄
    for i in range(M):

        # 길이 초기값 설정
        col_len = 0
        for j in range(N):
            if map_picture[j][i]:
                col_len += 1
                if highest_len < col_len:
                    highest_len = col_len
            else:
                col_len = 0

    print(highest_len)

