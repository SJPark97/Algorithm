queue_melt = set()
queue_melt.update(((0, 0), (2, 0), (0, 2), (2, 2)))
# if (0, 3) not in queue_melt:
#     queue_melt.add((0, 3))
# queue_melt.add((0, 2))
for (x, y) in queue_melt:
    print(x, y)


def melt(board2):
    global board
    queue_melt = set()
    queue_melt.update(((0, 0), (N2 - 1, 0), (0, N2 - 1), (N2 - 1, N2 - 1)))
    for i in range(N2):
        for j in range(N2):
            if board2[i][j] == 0:
                for n in range(len(dx)):
                    mx, my = i + dx[n], j + dy[n]
                    if 0 <= mx < N2 and 0 <= my < N2 and board2[mx][my] > 0:
                        queue_melt.add((mx, my))
    for (x, y) in queue_melt:
        cnt = 0

        for n in range(len(dx)):
            mx, my = x + dx[n], y + dy[n]
            if 0 <= mx < N2 and 0 <= my < N2 and board2[mx][my] > 0:
                cnt += 1
            if cnt == 3:
                break
        if cnt < 3:
            board2[x][y] -= 1
    board = [item[:] for item in board2]
    return cnt