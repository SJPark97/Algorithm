import sys

sys.stdin = open("input.txt")

n = int(input())
for test_case in range(1, n + 1):
    print(f'#{test_case}', end=' ')
    card_num = list(input())
    number_list = [0] * 10
    result = 0
    run = 0
    for card in card_num:
        number_list[int(card)] += 1
    for triplet_count in range(10):
        while number_list[triplet_count] >= 3:
            number_list[triplet_count] -= 3
            result += 1
        # if number_list[triplet_count] == 6:
        #     result += 2
        # elif number_list[triplet_count] >= 3:
        #     result += 1
        #     number_list[triplet_count] -= 3
    for run_count in number_list:
        if run_count:
            run += 1
        else:
            if run == 6:
                result += 2
            elif run >= 3:
                result += 1
            else:
                run = 0
    if result >= 2:
        print(1)
    else:
        print(0)
