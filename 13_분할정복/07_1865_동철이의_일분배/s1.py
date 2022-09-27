import sys

sys.stdin = open('input.txt')


def sol():
    def dfs(work, percent):
        nonlocal visit, result
        if result >= percent:
            return
        if work == n:
            if result < percent:
                result = percent
            return

        for i in range(n):
            if not visit[i] and works[work][i] != 0:
                visit[i] = True
                dfs(work + 1, percent * works[work][i] * 0.01)
                visit[i] = False
        return

    n = int(input())
    works = [list(map(int, input().split())) for _ in range(n)]
    visit = [False] * n
    result = 0
    dfs(0, 100)
    answer.append('#{0} {1:0.6f}'.format(test_case, result))


answer = []
for test_case in range(1, int(input()) + 1):
    sol()
print(*answer, sep="\n")
