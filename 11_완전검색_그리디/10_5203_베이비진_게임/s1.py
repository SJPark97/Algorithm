from itertools import combinations


def comb(li):
    for chk_list in combinations(sorted(li), 3):
        if len(set(chk_list)) == 1 or chk_list[0] + 2 == chk_list[1] + 1 == chk_list[2]:
            return True
    return False


def sol():
    player_1 = []
    player_2 = []
    cards = list(map(int, input().split()))
    answer = 0
    for i in range(12):
        if i % 2:
            player_2.append(cards[i])
        else:
            player_1.append(cards[i])
    for i in range(3, 7):
        if comb(player_1[:i]):
            answer = 1
            break
        if comb(player_2[:i]):
            answer = 2
            break
    print(answer)
    return


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
