import sys

sys.stdin = open('input.txt')


def sol():
    def find(number):
        start = 0
        end = len(list_a) - 1
        signal = 0
        while True:
            middle = (start + end) // 2
            if list_a[middle] == number:
                return True
            elif list_a[middle] < number:
                if signal == 1:
                    return False
                signal = 1
                start = middle + 1
            else:
                if signal == 2:
                    return False
                signal = 2
                end = middle - 1

    n, m = map(int, input().split())
    list_a = tuple(sorted(list(map(int, input().split()))))
    list_b = list(map(int, input().split()))
    answer = 0
    for num in list_b:
        if num in list_a and find(num):
            answer += 1
    print(answer)


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
