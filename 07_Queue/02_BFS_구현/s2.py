
def bfs(start):
    visit[start] = True
    queue = [start]
    print(start, end=' ')

    while queue:
        start = queue.pop(0)
        for next in way[start]:
            if not visit[next]:
                visit[next] = True
                queue.append(next)
                print(next, end=' ')


n, m = map(int, input().split())
way_list = list(map(int, input().split()))
way = [[] for _ in range(n+1)]
visit = [False] * (n+1)

for i in range(0, len(way_list), 2):
    way[way_list[i]].append(way_list[i+1])
    way[way_list[i+1]].append(way_list[i])

bfs(1)

