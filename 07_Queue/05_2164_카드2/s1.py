# 규칙 찾아내서 풀기 (통과)
N = int(input())
if N == 1:
    print(N)
else:
    card_list = list(range(0, N+1, 2))
    for i in range(1, 20):
        if N <= 2**i:
            print(card_list[N - 2**(i-1)])
            break

# 큐로 풀기 (시간초과)
N = int(input())
card_list = list(range(1, N+1))

while len(card_list) > 1:
    card_list.pop(0)
    card_list.append(card_list.pop(0))
print(card_list[0])

# 덱으로 풀기 (통과)
from collections import deque

n = int(input())
queue = deque(range(1, n + 1))

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])

# 신기한 풀이 1번이랑 비슷한데 더 스마트함
n = int(input())

a = 1
while n > a * 2:
    a *= 2

print((n - a) * 2 or n)