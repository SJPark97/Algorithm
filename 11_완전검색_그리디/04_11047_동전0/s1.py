def sol():
    n, k = map(int, input().split())
    answer = 0
    for coin in [int(input()) for _ in range(n)][::-1]:
        if k == 0:
            break
        chk = k // coin
        if chk != 0:
            answer += chk
            k %= coin
    print(answer)


sol()
