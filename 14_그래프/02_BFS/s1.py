from collections import deque


def sol():
    def bfs(start):
        queue = deque([start])
        visit[start] = True
        while queue:
            num = queue.popleft()
            print(num, end=" ")
            for n in board[num]:
                if not visit[n]:
                    visit[n] = True
                    queue.append(n)

    nums = list(map(int, input().split()))
    board = [[] for _ in range(8)]
    for i in range(0, len(nums), 2):
        board[nums[i]].append(nums[i + 1])
        board[nums[i + 1]].append(nums[i])
    visit = [False] * 8
    bfs(1)


sol()
