import sys

sys.stdin = open('input.txt')


def sol():
    n = int(input())
    a = round(n**(1/3))
    if a**3 == n:
        print(a)
        return
    print(-1)
    return


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
