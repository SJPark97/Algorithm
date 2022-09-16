from collections import deque
import sys

sys.stdin = open('input.txt')


def bfs():
    queue = deque([(people_start, 0)])
    result = []
    visit[people_start] = True
    while queue:
        a, t = queue.popleft()
        for j in people_list[a]:
            if not visit[j]:
                visit[j] = True
                queue.append((j, t+1))
                result.append((j, t+1))
    result.sort(key=lambda x: (x[1], x[0]))
    return result[-1][0]


for test_case in range(1, 11):
    print(f'#{test_case}', end=" ")
    length, start = map(int, input().split())
    call_list = list(map(int, input().split()))
    people = sorted(list(set(call_list)))
    print(people)
    people_start = people.index(start)
    visit = [False] * len(people)
    people_list = [[] for _ in range(len(people))]
    for i in range(0, length, 2):
        people_list[people.index(call_list[i])].append(people.index(call_list[i+1]))
    people_list = list(map(sorted, people_list))
    print(people[bfs()])
