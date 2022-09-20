n = int(input())
result = [[] for _ in range(n)]
cord = ('001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111')
for t in range(n):
    h_num = input()
    b_num = bin(int(h_num, 16))[2:]
    b_num = '0' * (len(h_num) * 4 - len(b_num)) + b_num
    for i in range(len(b_num)):
        if b_num[i:i + 6] in cord:
            start = i
            break
    for j in range(start, len(b_num), 6):
        chk = b_num[j:j + 6]
        if len(chk) == 6:
            result[t].append(cord.index(b_num[j:j + 6]))
for j in range(n):
    print(*result[j])
