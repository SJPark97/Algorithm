for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    n, m = map(int, input().split())
    container = sorted(list(map(int, input().split())))[::-1]
    truck = sorted(list(map(int, input().split())))[::-1]
    answer = 0
    for t in truck:
        for i in range(len(container)):
            if t >= container[i]:
                answer += container[i]
                del container[i]
                break
    print(answer)