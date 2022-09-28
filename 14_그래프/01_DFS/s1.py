def sol():
    def dfs(number):
        print(number, end=" ")
        visit[number] = True
        for n in board[number]:
            if not visit[n]:
                dfs(n)
        return

    nums = list(map(int, input().split()))
    board = [[] for _ in range(8)]
    for i in range(0, len(nums), 2):
        board[nums[i]].append(nums[i + 1])
        board[nums[i + 1]].append(nums[i])
    visit = [False] * 8
    dfs(1)


sol()
