n = int(input())
result = [[] for _ in range(n)]
for t in range(n):
    h_num = input()
    b_num = bin(int(h_num, 16))[2:]
    b_num = '0' * (len(h_num) * 4 - len(b_num)) + b_num
    for i in range(0, len(b_num), 7):
        result[t].append(int(b_num[:7], 2))
        b_num = b_num[7:]
    if b_num:
        result[t].append(int(b_num, 2))
for j in range(n):
    print(*result[j])