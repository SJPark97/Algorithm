def stacksystem(number):
    if number == 0:
        if len(stack) != 0:
            return stack.pop()
        else:
            return
    else:
        return stack.append(number)

T = int(input())
stack = []

for _ in range(T):
    number = int(input())
    stacksystem(number)

print(sum(stack))