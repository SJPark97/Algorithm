import sys

sys.stdin = open("input.txt")

# T = int(input())
#
# for test_case in range(1, T+1):
#     print(f'#{test_case}', end=' ')
#
#     N, M = map(int, input().split())
#
#     pizza_list = list(map(int, input().split()))
#     pizza_num = list(range(1, M+1))
#
#     pizza_list_num = list(zip(pizza_list, pizza_num))
#
#     fire = pizza_list_num[:N]
#     pizza_list_num = pizza_list_num[N:]
#
#     while len(fire) != 1:
#         check = list(fire.pop(0))
#         check[0] = check[0]//2
#         if check[0] == 0:
#             if pizza_list_num:
#                 fire.append(pizza_list_num.pop(0))
#         else:
#             fire.append(check)
#
#     print(fire[0][1])
#

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    N, M = map(int, input().split())

    pizza_list = list(map(int, input().split()))
    pizza_num = list(range(1, M + 1))
    pizza_list_num = list(map(list, zip(pizza_list, pizza_num)))

    while len(pizza_list_num) > 1:
        cnt = N
        delete = []
        for m in range(M):
            if m < len(pizza_list_num):
                if pizza_list_num[m][0] != 0:
                    pizza_list_num[m][0] = pizza_list_num[m][0]//2
                    cnt -= 1
                else:
                    delete.append(m)
                if cnt == 0:
                    break

        for num in delete[::-1]:
            if len(pizza_list_num) > 1:
                del pizza_list_num[num]
    print(pizza_list_num[0][1])