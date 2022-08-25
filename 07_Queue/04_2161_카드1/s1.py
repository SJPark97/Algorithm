
N = int(input())
card_list = list(range(1, N+1))
print(card_list.pop(0), end=' ')
while card_list:
    card_list.append(card_list.pop(0))
    print(card_list.pop(0), end=' ')
