from itertools import permutations, combinations
import sys
sys.stdin = open('input.txt')


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    food_numbers = int(input())
    food_list = list(range(food_numbers))
    s = [list(map(int, input().split())) for _ in range(food_numbers)]
    food_flavor = []
    comb = list(combinations(food_list, food_numbers//2))
    for foods in comb:
        cnt = 0
        for x, y in list(permutations(foods, 2)):
            cnt += s[x][y]
        food_flavor.append(cnt)
    flavor = []
    for i in range(len(comb)//2):
        flavor.append(abs(food_flavor[i]-food_flavor[-i-1]))
    print(min(flavor))
