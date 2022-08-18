def pascal(n):
    if n == 1:
        pascal_list[0].extend([1, 0])
    else:
        pascal(n - 1)
        for i in range(n):
            pascal_list[n-1].append(pascal_list[n-2][i]+pascal_list[n-2][i+1])
        pascal_list[n-1].append(0)




T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}')

    N = int(input())
    pascal_list = [[0] for _ in range(N)]
    pascal(N)
    for i in pascal_list:
        print(*i[1:-1])
