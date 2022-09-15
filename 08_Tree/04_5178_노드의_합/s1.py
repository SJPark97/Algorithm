import sys

sys.stdin = open('input.txt')


def sol():
    n, m, l = map(int, input().split())
    node = [0]*(n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        node[a] = b
    if n % 2 == 0:
        node[n//2] = node[n]
        n -= 1
    for i in range(n, 1, -2):
        node[i//2] = node[i-1]+node[i]
    print(node[l])
    return


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()