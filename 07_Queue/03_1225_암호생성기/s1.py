import sys

sys.stdin = open("input.txt")

for test_case in range(1, 11):
    print(f'#{test_case}', end=' ')
    case = int(input())
    case_num = list(map(int, input().split()))

    while case_num[-1]:
        for i in range(1, 6):
            x = case_num.pop(0)
            if x - i <= 0:
                case_num.append(0)
                break
            else:
                case_num.append(x-i)

    print(*case_num)
