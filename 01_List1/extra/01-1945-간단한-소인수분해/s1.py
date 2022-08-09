import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}', end = ' ')
    N = int(input())
    alph = [2, 3, 5, 7, 11]
    count = [0] * 5
    for num in range(5):
        while True:
            if N % alph[num] == 0:
                N = N / alph[num]
                count[num] += 1
            else:
                break
    print(*count)
