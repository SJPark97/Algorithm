import sys

sys.stdin = open('input.txt')


def lvr(node):
    if node < len(tree):
        lvr(node*2)
        print(tree[node], end="")
        lvr(node*2 + 1)


def sol():
    for _ in range(int(input())):
        inp = list(input().split())
        tree.append(inp[1])
    lvr(1)
    print()


for test_case in range(1, 11):
    print(f'#{test_case}', end=" ")
    tree = [0]
    sol()