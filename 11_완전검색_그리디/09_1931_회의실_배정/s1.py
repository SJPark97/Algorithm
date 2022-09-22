n = int(input())
time_list = [tuple(map(int, input().split())) for _ in range(n)]
time_list.sort(key=lambda x: (x[1], x[0]))
answer = 1
end = time_list[0][1]
for i in range(1, n):
    if time_list[i][0] >= end:
        end = time_list[i][1]
        answer += 1
print(answer)
