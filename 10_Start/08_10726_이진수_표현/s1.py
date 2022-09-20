# import sys
#
# sys.stdin = open('input.txt')


def sol():
    n, m = map(int, input().split())
    chk = bin(m)[2:]
    for i in range(n):
        if not int(chk) & (1 << i):
            print("OFF")
            return
    print("ON")
    return


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()