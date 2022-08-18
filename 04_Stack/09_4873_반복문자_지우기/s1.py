def dlt(n):
    if alph[n] == alph[n + 1]:
        del alph[n:n + 2]
        if not n:
            dlt(n)
        else:
            dlt(n-1)
            dlt(n)

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    alph = list(input())

    for index in range(len(alph)):
        try:
            dlt(index)
        except:
            break

    print(len(alph))
