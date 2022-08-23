
for t in range(1, int(input()) + 1):
    word = input()
    stack = []

    for char in word:
        if char not in '*/+-':
            stack.append(int(char))

        else:
            x = stack.pop()
            y = stack.pop()

            if char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
            elif char == '/':
                stack.append(y / x)
            elif char == '*':
                stack.append(y * x)

    print(f'#{t} {stack[-1]}')




