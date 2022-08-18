import sys

sys.stdin = open("input.txt")

for test_case in range(1, 11):
    print(f'#{input()}', end=' ')

    # 사다리 받아오기
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 움직임 설정
    dx = [0, 0, -1]
    dy = [-1, 1, 0]

    # 도착지 위치
    x = 99
    y = ladder[99].index(2)

    while True:
        # 좌측에 1이 있을 경우 좌측으로 무한 반복
        if 0 <= x + dx[0] < 100 and 0 <= y + dy[0] < 100 and ladder[x + dx[0]][y + dy[0]] == 1:
            while True:
                if 0 <= x + dx[0] < 100 and 0 <= y + dy[0] < 100 and ladder[x + dx[0]][y + dy[0]] != 0:
                    x += dx[0]
                    y += dy[0]
                else:
                    break
        # 우측에 1이 있을 경우 우측으로 무한 반복
        elif 0 <= x + dx[1] < 100 and 0 <= y + dy[1] < 100 and ladder[x + dx[1]][y + dy[1]] == 1:
            while True:
                if 0 <= x + dx[1] < 100 and 0 <= y + dy[1] < 100 and ladder[x + dx[1]][y + dy[1]] != 0:
                    x += dx[1]
                    y += dy[1]
                else:
                    break
        # 좌, 우에 길이 없으면 위로 한칸
        x += dx[2]
        y += dy[2]

        if x == 0:
            print(y)
            break
