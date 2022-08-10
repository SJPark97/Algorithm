import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')

    # list의 길이를 input으로 받기
    N = int(input())

    # input 값을 받아 list 생성
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 움직임 생성 (i, j)
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    # 결과값을 출력할 count 선언
    result = 0

    # 델타검색을 이용해 상하좌우를 찾아내 차의 절대값을 result에 입력
    for i in range(0, N):
        for j in range(0, N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    result += abs(arr[ni][nj] - arr[i][j])
    print(result)


