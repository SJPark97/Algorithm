import sys

sys.stdin = open('input.txt')


def behind(node, p, n):
    if node[p][0] in '+-*/':
        node[p] = chk(behind(node, int(node[p][1]), n), node[p][0], behind(node, int(node[p][2]), n))
    return node[p]


def chk(a, b, c):
    if b == '+':
        return str(round(int(a)+int(c)))
    elif b == '-':
        return str(round(int(a)-int(c)))
    elif b == '/':
        return str(round(int(a)/int(c)))
    elif b == '*':
        return str(round(int(a)*int(c)))


def sol():
    n = int(input())
    node = [0]
    for _ in range(n):
        add = list(input().split())
        if len(add) == 4:
            node.append(add[1:])
        else:
            node.append(add[1])
    print(behind(node, 1, n))


for test_case in range(1, 11):
    print(f'#{test_case}', end=" ")
    sol()
