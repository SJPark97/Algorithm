import sys

sys.stdin = open("input.txt")

def chk(k):
    know[k] = True
    for p in people[k]:
        if not know[p]:
            chk(p)

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    N, M = map(int, input().split())
    people = [[] for _ in range(N)]
    know = [False for _ in range(N)]
    count = 0

    for _ in range(M):
        v1, v2 = map(int, input().split())
        people[v1-1].append(v2-1)
        people[v2-1].append(v1-1)

    for k in range(N):
        if not know[k]:
            count += 1
            chk(k)

    print(count)
