def bfs(start_v):
    queue = [start_v]
    visit[start_v] = True
    count = 0

    while queue:
        now_v = queue.pop(0)
        for next_v in com[now_v]:
            if not visit[next_v]:
                visit[next_v] = True
                queue.append(next_v)
                count += 1
    return count


com_num = int(input())
node = int(input())
com = [[] for _ in range(com_num+1)]
visit = [False] * (com_num+1)

for _ in range(node):
    v1, v2 = map(int, input().split())
    com[v1].append(v2)
    com[v2].append(v1)

print(bfs(1))
