import sys

sys.stdin = open('input.txt')


def sol():
    def dfs(idx, rec):
        if rec == end:
            return 1
        if dp[rec]:
            return dp[rec]

        p = 0
        for i in range(n):
            if not (rec & (1 << i)) and works[idx][i] != 0:
                p = max(p, works[idx][i] / 100 * dfs(idx + 1, rec | (1 << i)))
        dp[rec] = p
        return p

    n = int(input())
    works = [list(map(int, input().split())) for _ in range(n)]
    end = (1 << n) - 1
    dp = [0] * end
    answer.append('#{0} {1:0.6f}'.format(test_case, 100 * dfs(0, 0)))


answer = []
for test_case in range(1, int(input()) + 1):
    sol()
print(*answer, sep="\n")
