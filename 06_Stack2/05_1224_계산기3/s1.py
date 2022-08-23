import sys

sys.stdin = open("input.txt")

for test_case in range(1, 11):
    len_word = input()
    word = input()
    result = ''
    stack = []

    for token in word:
        if token in '+-/*()':
            if not stack or token == '(':
                stack.append(token)

            elif token in '*/':
                while stack and stack[-1] in '*/':
                    result += stack.pop()
                stack.append(token)

            elif token in '+-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(token)

            elif token == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
        else:
            result += token
    while stack:
        result += stack.pop()

    for str in result:
        if str not in '+-*/':
            stack.append(int(str))

        else:
            x = stack.pop()
            y = stack.pop()

            if str == '+':
                stack.append(y + x)
            elif str == '-':
                stack.append(y - x)
            elif str == '*':
                stack.append(y * x)
            elif str == '/':
                stack.append(y / x)

    print(f'#{test_case} {stack[-1]}')



