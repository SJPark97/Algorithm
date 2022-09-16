from itertools import combinations
import sys

sys.stdin = open('input.txt')

def sol():
    n, b = map(int, input().split())
    length = list(map(int, input().split()))
    answer = b
    for i in range(n, 0, -1):
        for num in list(map(sum, list(combinations(length, i)))):
            chk = num - b
            if chk == 0:
                print(0)
                return

            if chk > 0 and answer > chk:
                answer = chk

    print(answer)
    return


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
