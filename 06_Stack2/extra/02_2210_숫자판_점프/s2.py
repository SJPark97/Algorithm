import sys

sys.stdin = open("input.txt")
# result에 없는 길이 6의 경로를 result에 추가하는 함수
def board_check(arr, x, y):
    # 만약 arr의 길이가 6이면
    if len(arr) == 6:
        # arr의 요소가 result에 없으면
        if tuple(arr) not in result:
            # result에 arr 추가
            result.add(tuple(arr))
        return

    for n in range(4):
        nx, ny = x + dx[n], y + dy[n]
        if 0 <= nx < 5 and 0 <= ny < 5:
            arr.append(board[x][y])
            board_check(arr, nx, ny)
            arr.pop()


board = [list(map(int, input().split())) for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# result를 set으로 하는 이유가 list보다 in연산을 할때 시간이 어마어마하게 이득이기 때문
result = set()
# board의 모든 위치에서 탐색
for i in range(5):
    for j in range(5):
        board_check([], i, j)
# result의 길이를 출력
print(len(result))

