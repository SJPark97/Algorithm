import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    #  5개의 글자를 모두 받는다
    all_text = [input() for _ in range(5)]

    #  최대 길이가 15니까 15번을 반복문을 돌리고 예외는 pass한다
    for i in range(15):
        for text in all_text:
            try:
                print(text[i], end='')
            except:
                pass
    print()
