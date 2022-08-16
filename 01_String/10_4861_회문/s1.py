#  list 이용
import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    #  N, N 값 받기
    N, M = map(int, input().split())
    string_list_row = [list(input()) for _ in range(N)]
    string_list_col = list(zip(*string_list_row))

    for i in range(N):
        for j in range(N-M+1):
            word_row = string_list_row[i][j:M+j]
            word_col = string_list_col[i][j:M+j]
            if word_row == word_row[::-1]:
                for k in range(M):
                    print(word_row[k], end='')
            elif word_col == word_col[::-1]:
                for k in range(M):
                    print(word_col[k], end='')
    print()
