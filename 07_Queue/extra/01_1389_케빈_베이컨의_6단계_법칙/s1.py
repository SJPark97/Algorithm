from collections import deque
import sys
sys.stdin = open("input.txt")


def kevin():
    for p in range(1, N+1):
        visit = [False] * (N+1)
        queue = deque([(p, 1)])
        result = 0
        visit[p] = True

        while queue:
            i, t = queue.popleft()
            for n in friends[i]:
                if not visit[n]:
                    visit[n] = True
                    result += t
                    queue.append((n, t+1))
        if p == 1:
            result_s = result
            result_p = p
        else:
            if result_s > result:
                result_s = result
                result_p = p
    print(result_p)


N, M = map(int, input().split())
friends = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    friends[v1].append(v2)
    friends[v2].append(v1)

kevin()

