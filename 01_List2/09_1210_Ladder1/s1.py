import sys

sys.stdin = open("input.txt")

for test_case in range(1, 11):
    print(f'#{input()}', end=' ')

    # 사다리 받아오기
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 움직임 설정
    dx = [0, 0, 1]
    dy = [-1, 1, 0]

    # 출발지의 수
    start_num = ladder[0].count(1)

    for start in range(start_num):

        # 출발 위치, 방향, 출발지 초기화, 중간 정지옵션
        x = 0
        y = ladder[0].index(1)
        start_location = ladder[0].index(1)
        ladder[x][y] = 0
        end_option = 0

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
            # 좌, 우에 길이 없으면 아래로 한칸
            x += dx[2]
            y += dy[2]

            # 목적지에 도달하면 시작 위치를 반환하고 종료옵션 = 1
            if ladder[x][y] == 2:
                end_option = 1
                print(start_location)
                break

            # 아래로 더 이동할 수 없을 때 반복문 종료
            elif x + dx[2] == 100:
                break
        if end_option:
            break
