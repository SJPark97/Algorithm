import sys
from collections import deque
sys.stdin = open("input.txt")

N, K = map(int, input().split())
velt = list(map(int, input().split()))
queue = deque(velt[::-1])
robot_location = deque([])
cnt = 0


while True:
    print(queue, robot_location)
    chk = queue.popleft()
    for _ in range(len(robot_location)):
        i = robot_location.popleft()
        if queue[i - 2] > 0 and i - 2 > N:
            queue[i - 2] -= 1
            robot_location.append(i - 2)
        elif i - 1 > N and queue[i - 2] == 0:
            robot_location.append(i - 1)
    if chk > 0:
        robot_location.append(2*N-1)
        queue.append(chk - 1)
    else:
        queue.append(chk)
    cnt += 1
    print(queue, robot_location)
    print()
    if queue.count(0) >= K:
        break


print(cnt)