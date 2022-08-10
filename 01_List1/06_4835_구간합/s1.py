import sys

sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    N, M = map(int, input().split())
    number_list = list(map(int, input().split()))
    number = [0] * (N-M+1)                      #M개씩 합쳐서 넣을 리스트 만들기
    for range_num in range(0, N-M+1):           #M개씩 합쳐서 리스트에 입력
        count_num = 0
        for num in range(range_num, range_num + M):
            count_num += number_list[num]
        number[range_num] = count_num
    for i in range(len(number)-1, 0, -1):       #합의 리스트 정렬
        for j in range(0, i):
            if number[j] > number[j+1]:
                number[j], number[j+1] = number[j+1], number[j]
    answer = number[-1] - number[0]             #최대 최소 차
    print(answer)
