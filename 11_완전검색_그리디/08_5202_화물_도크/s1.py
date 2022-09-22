def dfs(s, t):
    global answer
    for j in range(s + 1, n):
        if time_list[j][0] >= time_list[s][1]:
            dfs(j, t + 1)
    if answer < t:
        answer = t
    return


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    n = int(input())
    time_list = [tuple(map(int, input().split())) for _ in range(n)]
    time_list.sort(key=lambda x: (x[0], x[1]))
    answer = -1
    for i in range(n):
        if n - i > answer:
            dfs(i, 1)
    print(answer)