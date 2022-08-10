import sys

sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    N = int(input())
    cards = input()             #카드를 문자열로 받기
    card_list = [[0 for col in range(2)] for row in range(10)]  #카드 리스트 생성
    for card in cards:
        card_num = int(card)
        card_list[card_num][0] = card_num
        card_list[card_num][1] += 1
    for i in range(len(card_list) - 1, 0, -1):                  #카드 개수가 많은걸 우로 밀기
        for j in range(0, i):
            if card_list[j][1] > card_list[j + 1][1]:           #개수가 같으면 카드의 숫자가 낮은건 왼
                card_list[j], card_list[j + 1] = card_list[j + 1], card_list[j]
    print(card_list[-1][0], card_list[-1][1])