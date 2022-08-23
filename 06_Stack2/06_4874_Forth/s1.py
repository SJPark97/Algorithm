import sys

sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')

    word = input().split()
    stack = []
    for char in word:
        if char not in '+-*/. ':
            stack.append(int(char))
        elif char == '.':
            if len(stack) == 1:
                result = stack[-1]
            else:
                result = 'error'
        else:
            if len(stack) > 1:
                x = stack.pop()
                y = stack.pop()

                if char == '+':
                    stack.append(y + x)
                elif char == '-':
                    stack.append(y - x)
                elif char == '*':
                    stack.append(y * x)
                elif char == '/':
                    stack.append(y // x)
            else:
                result = 'error'
                break
    print(result)



