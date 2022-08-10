import sys

sys.stdin = open("input.txt")

T = int(input())

for bus_case in range (1, T + 1):
    print(f'#{bus_case}', end=' ')
    K, N, M = map(int, input().split())
    charger_list = list(map(int, input().split())) #충전기 위치
    bus_list = [0] * (N + 1) #정류장 생성
    for charger in charger_list: #정류장과 충전기 위치 표시
        bus_list[charger] = 1
    location = 0 #위치 생성
    counter = 0  # counter 생성
    while location < N:
        for move in range(K, 0, -1):
            if location + move >= N:                #종점에 도달하면 위치를
                print(counter)                      #종점에 이동시키고 종료
                location = N
                break
            elif bus_list[location + move] == 1:    #만약 버스의 움직임
                location = location + move          #위치에 충전기가 있을 경우
                counter += 1                        #counter 1하고 반복
                break
            elif move == 1:                         #만약 버스의 움직임
                print(0)                            #위치에 충전기가 없을 경우
                location = N                        #0을 출력하고 종료
				# 버스 움직임 위치에 충전기가 없을 경우 패스 (따로 코드는 없음)