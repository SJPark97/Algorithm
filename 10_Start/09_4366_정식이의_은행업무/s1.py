def sol():
    bin_num = input()
    ter_num = input()
    bin_num_10 = int(bin_num, 2)
    ter_num_10 = int(ter_num, 3)
    bin_num = bin_num[::-1]
    ter_num = ter_num[::-1]
    chk = set()
    for i in range(len(bin_num) - 1):
        chk.add(str(bin_num_10 + ((-1) ** int(bin_num[i])) * (2 ** i)))
    for i in range(len(ter_num)):
        a = int(ter_num[i])
        ck = ter_num_10 - (3 ** i) * a
        for j in range(1, 3):
            b = str(ck + (3 ** i) * ((a + j) % 3))
            if b in chk:
                print(b)
                return


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=' ')
    sol()
