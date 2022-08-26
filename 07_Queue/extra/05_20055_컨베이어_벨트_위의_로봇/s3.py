import sys
from collections import deque
sys.stdin = open("input.txt")

N, K = map(int, input().split())
velt = list(map(int, input().split()))
queue = deque(velt[::-1])
robot_location = deque([])
cnt = 0

while True:
    cnt += 1
    print(queue, robot_location)
    for _ in range(len(robot_location)):
        i = robot_location.popleft() - 1
        if i <= -N:
            continue
        if queue[i] == 0:
            robot_location.append(i)
        elif i > -N:
            if queue[i] > 0 and robot_location.count(i-1) == 0:
                queue[i] -= 1
                robot_location.append(i-1)
            else:
                robot_location.append(i)
    chk = queue.popleft()
    if chk > 0:
        robot_location.append(-1)
        queue.append(chk - 1)
    else:
        queue.append(chk)
    print(queue, robot_location)
    print()

    if queue.count(0) >= K:
        break

print(cnt)