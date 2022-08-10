import sys

sys.stdin = open("input.txt")

for test_case in range(10):
    print(f'#{input()}', end=' ')

    # list 받기
    number_list = [list(map(int, input().split())) for _ in range(100)]

    # 가장 높은 값 설정
    highest_sum = 0

    # 대각선 초기 값 설정정
    diago1_sum = 0
    diago2_sum = 0

    for i in range(100):
        
        # 대각선 값 더해서 저장
        diago1_sum += number_list[i][i]
        diago2_sum += number_list[-i][-i]

        # 행의 값을 더해서 가장 높은값과 비교 후 더 높으면 저장
        row_sum = sum(number_list[i])
        if highest_sum < row_sum:
            highest_sum = row_sum
        
        # 열의 값을 더해서 가장 높은값과 비교 후 더 높으면 저장
        col_sum = 0
        for j in range(100):
            col_sum += number_list[j][i]
        if highest_sum < col_sum:
            highest_sum = col_sum

    # 반복문 해제 후 더해진 대각선 값과 가장 높은값과 비교 후 더 높으면 저장
    if highest_sum < diago1_sum:
        highest_sum = diago1_sum

    if highest_sum < diago2_sum:
        highest_sum = diago2_sum

    print(highest_sum)
