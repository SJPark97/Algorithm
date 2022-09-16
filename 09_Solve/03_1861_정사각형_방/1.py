import sys
sys.setrecursionlimit(2500*1000)
sys.stdin = open('input.txt')


dx = [0, 1, 0, -1]  # 우 하 좌 상
dy = [1, 0, -1, 0]


def bfs(x, y):
    # 방문 처리
    d = 0
    queue = [(x, y, d + 1)]
    while queue:
        x, y, d = queue.pop(0)  # d = 이동거리
        # 델타검색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] - matrix[x][y] == 1:
                queue.append((nx, ny, d + 1))
                break
    return d


def solution(n, arr):  # 방번호와 최대 이동개수를 출력해야함
    value = 0
    index = 1000000 + 1
    for i in range(n):
        for j in range(n):
            v = bfs(i, j)
            if v > value:
                value = v
                index = arr[i][j]
            elif v == value and index > arr[i][j]:
                index = arr[i][j]

    return f'{index} {value}'


for case in range(1, 1 + int(input())):
    N = int(input())  # 행렬 길이, (1 ≤ N ≤ 1000)
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{case} {solution(N, matrix)}')  # 방번호와 최대 이동개수