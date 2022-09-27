def sol():
    def VLR(n):
        if n > 0:
            print(n, end=" ")
            VLR(board[n][0])
            VLR(board[n][1])
        return

    def LVR(n):
        if n > 0:
            LVR(board[n][0])
            print(n, end=" ")
            LVR(board[n][1])
        return

    def LRV(n):
        if n > 0:
            LRV(board[n][0])
            LRV(board[n][1])
            print(n, end=" ")
        return

    v, line = map(int, input().split())
    inp = list(map(int, input().split()))
    board = [[0, 0, 0] for _ in range(v + 1)]  # LRV
    for i in range(line):
        if board[inp[2 * i]][0] == 0:
            board[inp[2 * i]][0] = inp[2 * i + 1]
        else:
            board[inp[2 * i]][1] = inp[2 * i + 1]
        board[inp[2 * i + 1]][2] = inp[2 * i]
    for i in range(1, v + 1):
        if board[i][2] == 0:
            start = i
            break
    print("전위 순회 :", end=" ")
    VLR(start)
    print()
    print("중위 순회 :", end=" ")
    LVR(start)
    print()
    print("후위 순회 :", end=" ")
    LRV(start)


sol()
