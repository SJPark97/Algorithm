n = int(input())
result = [[] for _ in range(n)]
for t in range(n):
    num = input()
    for i in range(0, len(num), 7):
        result[t].append(int(num[i:i+7], 2))
for j in range(n):
    print(*result[j])