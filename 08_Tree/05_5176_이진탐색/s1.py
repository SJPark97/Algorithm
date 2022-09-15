import sys

sys.stdin = open('input.txt')


def lvr(node, p, n):
    global count
    if p*2 <= n:
        lvr(node, p*2, n)
    count += 1
    node[p] = count
    if p*2+1 <= n:
        lvr(node, p*2+1, n)
    return


def sol():
    n = int(input())
    node = [0] * (n+1)
    lvr(node, 1, n)
    print(node[1], node[n//2])
    return


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    count = 0
    sol()
