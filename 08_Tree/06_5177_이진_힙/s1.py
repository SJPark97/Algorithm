import sys

sys.stdin = open('input.txt')


def min_heap(node):
    l = len(node)-1
    while node[l] < node[l//2]:
        node[l], node[l//2] = node[l//2], node[l]
        l //= 2


def sol():
    node = [0]
    n = int(input())
    add_list = list(map(int, input().split()))
    for add in add_list:
        node.append(add)
        if len(node) > 2:
            min_heap(node)
    result = 0
    while n > 0:
        n //= 2
        result += node[n]
    print(result)
    return


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()