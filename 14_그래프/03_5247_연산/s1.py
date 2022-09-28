from collections import deque


def sol():
    def bfs(num, t):
        queue = deque([(num, t)])
        visit.add(num)
        while queue:
            number, times = queue.popleft()
            if number == m:
                return times
            for i in range(3):
                d_number = number + dx[i]
                if d_number <= 1000000 and d_number not in visit:
                    visit.add(d_number)
                    queue.append((d_number, times + 1))
            d_number = number * 2
            if d_number <= 1000000 and d_number not in visit:
                visit.add(d_number)
                queue.append((d_number, times + 1))
        return

    n, m = map(int, input().split())
    if n > m:
        n -= m
        if n % 10 <= 5:
            print(n // 10 + n % 10)
        else:
            print(n // 10 - n % 10 + 11)
        return
    visit = set()
    print(bfs(n, 0))


dx = [-10, -1, 1]
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=' ')
    sol()
