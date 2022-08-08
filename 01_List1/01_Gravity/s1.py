import sys

sys.stdin = open("input.txt")


case = int(input())
for test_case in range(1, case + 1):
    print(f'#{test_case}', end=' ')
    N = int(input())
    Box = list(map(int, input().split()))
    count = 0
    for B_number in range(N):
        high_box = 0

        for B_num in range(B_number + 1, N):
            if Box[B_number] > Box[B_num]:
                high_box += 1

        if count < high_box:
            count = high_box

    print(count)



