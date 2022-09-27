import sys

sys.stdin = open('input.txt')


def sol():
    n = int(input())
    board = [list(map(int, list(input()))) for _ in range(n)]


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
