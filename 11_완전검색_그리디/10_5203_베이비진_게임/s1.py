from itertools import combinations


def chk(li):
    return li[0] == li[1] == li[2] or li[0] + 2 == li[1] + 1 == li[2]


def comb(li):
    for chk_list in combinations(sorted(li), 3):
        if chk(chk_list):
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
        p1 = comb(player_1[:i])
        p2 = comb(player_2[:i])
        if p1:
            answer = 1
            break
        if p2:
            answer = 2
            break
    print(answer)
    return


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
