import sys

sys.stdin = open("input.txt")

def paper(n):
    if len(memo) <= n:
        if n % 2:
            memo.append(paper(n - 1) * 2 - 1)
        else:
            memo.append(paper(n - 1) * 2 + 1)
    return memo[n]

T = int(input())

memo = [0, 1]

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    N = int(input())
    n = N // 10
    print(paper(n))
