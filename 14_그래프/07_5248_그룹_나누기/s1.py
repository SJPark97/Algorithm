from collections import deque


def sol():
    def bfs(num):
        visit[num] = True
        queue = deque([num])
        while queue:
            num = queue.popleft()
            for people in board[num]:
                if not visit[people]:
                    visit[people] = True
                    queue.append(people)
        return 1

    n, m = map(int, input().split())
    board = [[] for _ in range(n + 1)]
    visit = [False] * (n + 1)
    nums = list(map(int, input().split()))
    for i in range(0, 2 * m, 2):
        board[nums[i]].append(nums[i + 1])
        board[nums[i + 1]].append(nums[i])
    answer = 0
    for i in range(1, n + 1):
        if not visit[i]:
            answer += bfs(i)
    print(answer)


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
