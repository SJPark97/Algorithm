import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    str1 = input()
    str2 = input()

    if str2.count(str1):
        print(1)
    else:
        print(0)
