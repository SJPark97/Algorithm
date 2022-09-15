# def lvr(node):
#     if node != 0:
#         print(node, end=" ")
#         lvr(tree[node][0])
#         lvr(tree[node][1])
#
#
# n = int(input())
# node_list = list(map(int, input().split()))
# tree = [[0, 0, 0] for _ in range(n+1)] # [L, R, V]
# for i in range(0, len(node_list), 2):
#     for j in range(2):
#         if tree[node_list[i]][j] == 0:
#             tree[node_list[i]][j] = node_list[i+1]
#             break
#     if tree[node_list[i+1]][2] == 0:
#         tree[node_list[i+1]][2] = node_list[i]
# lvr(1)


def lvr(node):
    print(node, end=" ")
    for i in range(2):
        if tree[node][i] != 0:
            lvr(tree[node][i])


n = int(input())
node_list = list(map(int, input().split()))
tree = [[0, 0, 0] for _ in range(n+1)] # [L, R, V]
for i in range(0, len(node_list), 2):
    for j in range(2):
        if tree[node_list[i]][j] == 0:
            tree[node_list[i]][j] = node_list[i+1]
            break
    if tree[node_list[i+1]][2] == 0:
        tree[node_list[i+1]][2] = node_list[i]
for x in range(1, n+1):
    if tree[x][2] == 0:
        lvr(x)
        break