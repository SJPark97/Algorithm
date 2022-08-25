import sys

sys.stdin = open("input.txt")

# 버스의 최소 교체시간 확인 함수
def bus_check(x, cnt):
    global result
    # cnt가 result값보다 커지면 종료
    if cnt >= result:
        return
    # 정류장이 갈 수 있는 수만큼 탐색
    for i in range(1, track[x]+1):
        # 만약 정류장이 갈 수 있는 수 + 시작위치가 종점보다 작을때
        if x+i < track[0]:
            # 시작위치를 바꾸고 cnt += 1
            bus_check(x+i, cnt+1)
        # 만약 정류장이 갈 수 있는 수 + 시작위치가 종점보다 높거나 같을때
        else:
            # result에 저장된 값보다 cnt가 작으면 cnt를 result에 저장
            if result > cnt:
                result = cnt


T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    track = list(map(int, input().split()))
    # track[0]이 정류장의 개수니까 최대값 설정
    result = track[0]
    # track[1]이 출발지점이니까 출발지점 1, cnt 0 설정
    bus_check(1, 0)
    print(result)