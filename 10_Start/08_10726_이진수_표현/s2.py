for test_case in range(int(input())):
    print(f"#{test_case}", sep=" ")
    N, M = map(int, input().split())
    if M % (2 ** N) == 2 ** N - 1:
        print('ON')
    else:
        print('OFF')
