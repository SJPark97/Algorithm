import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}')

    # 필요 없는 것들 받아서 사용 x
    remove = input()

    # word 받아오기, 정렬할 list 생성
    word = input()
    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    # number의 개수를 세서 순서대로 출력 (없으면 개수가 0이므로 출력되지 않음)
    for number in numbers:
        print((number+' ') * word.count(number), end='')

    # test_case 끼리의 개행을 위해 추가
    print()
