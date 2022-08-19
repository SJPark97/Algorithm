import sys

sys.stdin = open("input.txt")

T = int(input())
finish = ['.', '?', '!']
for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    n = int(input())
    word = input().split()
    count = 0
    result = []

    for chk_name in word:
        if chk_name[-1] not in finish:
            if chk_name == chk_name.title() and chk_name.isalpha():
                count += 1
        else:
            if chk_name == chk_name.title() and chk_name[:-1].isalpha():
                count += 1
            result.append(count)
            count = 0
    print(*result)