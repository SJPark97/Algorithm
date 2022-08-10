import sys

sys.stdin = open("input.txt")

for test_case in range(1, 11):
    print(f'#{test_case}', end=' ')
    count = int(input())
    box_list = list(map(int, input().split()))
    while count > 0:
        for i in range(len(box_list) - 1, 0, -1):       #정렬
            for j in range(0, i):
                if box_list[j] > box_list[j + 1]:
                    box_list[j], box_list[j + 1] = box_list[j + 1], box_list[j]
        if box_list[-1] - box_list[0] <= 1:             #최대 최소 차이가 1 이하면 break
            break
        box_list[0] += 1
        box_list[-1] -= 1
        count -= 1
    if box_list[0] < box_list[1]:                       #첫 박스와 두번째 박스 크기 비교
        box_min = box_list[0]
    else:
        box_min = box_list[1]
    if box_list[-1] > box_list[-2]:                     #마지막 박스와 마지막에서 두번째 박스 크기 비교
        box_max = box_list[-1]
    else:
        box_max = box_list[-2]
    answer = box_max - box_min
    print(answer)