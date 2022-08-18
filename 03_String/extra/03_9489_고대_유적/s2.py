# 포기

import sys

sys.stdin = open("input.txt")


# def func(a, b, c):
#     highest_len = 0
#     if c:
#         d, f = a, b
#     else:
#         d, f = b, a
#
#     for i in range(d):
#
#         # 길이 초기값 설정
#         length = 0
#         for j in range(f):
#             if c:
#                 x, y = i, j
#             else:
#                 x, y = j, i
#             if map_picture[x][y]:
#                 length += 1
#                 if highest_len < length:
#                     highest_len = length
#             else:
#                 length = 0
#     return highest_len
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     print(f'#{test_case}', end=' ')
#
#     # N, M, 사진 받아오기
#     N, M = map(int, input().split())
#     map_picture = [list(map(int, input().split())) for _ in range(N)]
#
#     # func을 이용하여 가로 가장 높은 값 세로 가장 높은 값 가져와서 비교 후 출력
#     # 1이 가로 0이 세로
#     high_len = [func(N, M, 1), func(N, M, 0)]
#     print(max(high_len))

def get_highest(board):
    highest_len = 0

    for line in board:
        length = 0
        for unit in line:
            if unit == 1:
                length += 1
                if highest_len < length:
                    highest_len = length
            else:
                length = 0

    return highest_len


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    map_picture = [list(map(int, input().split())) for _ in range(N)]

    row_highest = get_highest(map_picture)
    col_highest = get_highest(list(zip(*map_picture)))

    print(f'#{test_case} {max(row_highest, col_highest)}')