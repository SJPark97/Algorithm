import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    # 숫자의 길이, 숫자들의 list 받아서 정렬하기
    N = int(input())
    num_list = sorted(list(map(int, input().split())))

    # 뒤에서 하나 앞에서 하나 번갈아가면서 5개씩 출력하기
    for i in range(5):
        print(num_list[-(i+1)], end=' ')
        print(num_list[i], end=' ')
    print()




