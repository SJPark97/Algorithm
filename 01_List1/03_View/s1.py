import sys

sys.stdin = open("input.txt")

T = 10
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    test_len = int(input())
    building = list(map(int, input().split()))
    count = 0
    for case in range(2, test_len - 2):
        building_list = [building[case-2], building[case-1], building[case+1], building[case+2]]
        if building[case] > max(building_list):
            count += building[case] - max(building_list)
    #     difference = building[case] - building[case - 2]
    #     if difference > building[case] - building[case - 1]:
    #         difference = building[case] - building[case - 1]
    #     if difference > building[case] - building[case + 1]:
    #         difference = building[case] - building[case + 1]
    #     if difference > building[case] - building[case + 2]:
    #         difference = building[case] - building[case + 2]
    #     if difference > 0:
    #         count += difference
    print(count)