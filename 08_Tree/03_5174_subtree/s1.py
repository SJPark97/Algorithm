import sys

sys.stdin = open('input.txt')


def lvr(node, p):
    global count
    count += 1
    for i in range(2):
        if node[p][i] != 0:
            lvr(node, node[p][i])


def sol():
    e, n = map(int, input().split())
    node_list = list(map(int, input().split()))
    node = [[0, 0, 0] for _ in range(e+2)]  # [L R V]
    for i in range(e):
        node[node_list[i*2+1]][2] = node_list[i*2]
        for j in range(2):
            if node[node_list[i*2]][j] == 0:
                node[node_list[i*2]][j] = node_list[i*2+1]
                break
    lvr(node, n)
    print(count)
    return


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    count = 0
    sol()