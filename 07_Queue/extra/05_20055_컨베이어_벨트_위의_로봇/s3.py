import sys
from collections import deque
sys.stdin = open("input.txt")

N, K = map(int, input().split())
velt = list(map(int, input().split()))
# 마지막을 떼서 처음에 붙이니 list를 뒤집어서 처음을 떼서 마지막에 붙이게 만들기
queue = deque(velt[::-1])
# 로봇의 위치를 저장할 빈 list
robot_location = deque([])
# 횟수를 셀 cnt 설정
cnt = 0

while True:
    cnt += 1
    # 벨트 위에 올라간 로봇의 수만큼 반복
    # 첫 반복문때는 로봇의 수가 0이니까 무시됨
    for _ in range(len(robot_location)):
        # 로봇의 위치를 한칸 옮기기
        i = robot_location.popleft() - 1
        # 옮긴 위치가 벨트 끝이 아닐 경우
        # 주의!!!! 현재 벨트는 움직이지 않고 로봇의 위치만 변경되어서 엇나가있는 상태
        if i > -N:
            # 다음 위치가 0이 아니고 위치에 로봇이 없을 때 한칸 더 이동
            if queue[i] > 0 and robot_location.count(i-1) == 0:
                # 해당 위치 -1
                queue[i] -= 1
                # 한칸 더 이동한 위치가 벨트 끝일 경우 로봇 바로 제거
                if i - 1 > -N:
                    robot_location.append(i-1)
            # 다음 위치가 0일 경우 한칸 이동한걸 저장
            else:
                robot_location.append(i)
    # 벨트의 좌측을 제거
    chk = queue.popleft()
    # 해당 수가 0보다 클 경우 -1 해서 list에 추가 list의 마지막 위치에 로봇 추가
    if chk > 0:
        robot_location.append(-1)
        queue.append(chk - 1)
    # 해당 수가 0이하일 경우 그대로 list에 추가
    else:
        queue.append(chk)
    # 만약 0의 개수가 K이상일 경우 반복 끝
    if queue.count(0) >= K:
        break

print(cnt)