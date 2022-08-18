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

for test_case in range(1, 11):
    print(f'#{test_case}', end=' ')

    n, alph = input().split()
    alph = list(alph)
    for index in range(int(n)):
        try:
            dlt(index)
        except:
            break

    print(*alph, sep='')
