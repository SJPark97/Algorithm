import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    str1 = input()
    str1 = ''.join(set(str1))
    str2 = input()
    highest_cnt = 0

    for alph in str1:
        cnt = str2.count(alph)
        if cnt > highest_cnt:
            highest_cnt = cnt
    print(highest_cnt)
