
def virus(com_num):
    check[com_num] = True

    for next_m in com_graph[com_num]:
        if not check[next_m]:
            global total
            total += 1
            virus(next_m)


com = int(input())
node = int(input())
com_graph = [[] for _ in range(com+1)]
check = [False] * (com+1)
total = 0

for _ in range(node):
    v1, v2 = map(int, input().split())
    com_graph[v1].append(v2)
    com_graph[v2].append(v1)
virus(1)
print(total)


