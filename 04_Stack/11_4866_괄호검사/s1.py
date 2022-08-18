import sys

sys.stdin = open("input.txt")

def check_list(s):
    result = 0
    for check_s in s:
        if check_s in opn:
            stack.append(check_s)
        elif check_s in cls:
            if not stack:
                break
            elif opn.index(stack[-1]) == cls.index(check_s):
                stack.pop()
            else:
                break
    else:
        if not stack:
            result = 1
    return result

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    code = input()
    opn = ['(', '{']
    cls = [')', '}']
    stack = []
    print(check_list(code))
