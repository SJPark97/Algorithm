def sol():
    def stack():
        if not chk_list:
            return 0
        chk_list.sort(reverse=True)
        distance, x, y = chk_list.pop()
        answer = atom_list[x][3] + atom_list[y][3]
        chk = {x, y}
        while chk_list:
            d, x, y = chk_list.pop()
            if x not in chk and y not in chk:
                distance = d
                answer += atom_list[x][3] + atom_list[y][3]
                chk.update((x, y))
            elif distance == d:
                if x not in chk:
                    answer += atom_list[x][3]
                    chk.add(x)
                if y not in chk:
                    answer += atom_list[y][3]
                    chk.add(y)
        return answer

    for tc in range(1, int(input()) + 1):
        n = int(input())
        atom_list = [list(map(int, input().split())) for _ in range(n)]
        atom_list.sort()
        chk_list = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                dx = atom_list[i][0] - atom_list[j][0]
                dy = atom_list[i][1] - atom_list[j][1]
                if dy == 0:
                    if atom_list[i][2] == 3 and atom_list[j][2] == 2:
                        chk_list.append((-dx, i, j))
                elif dx == 0:
                    if (atom_list[i][2], atom_list[j][2]) == (0, 1) and dy < 0:
                        chk_list.append((-dy, i, j))
                    elif (atom_list[i][2], atom_list[j][2]) == (1, 0) and dy > 0:
                        chk_list.append((dy, i, j))
                elif dx == dy:
                    if atom_list[i][2] == 3 and atom_list[j][2] == 1 or atom_list[i][2] == 0 and atom_list[j][2] == 2:
                        chk_list.append((abs(dx) + abs(dy), i, j))
                elif dx == -dy:
                    if atom_list[i][2] == 3 and atom_list[j][2] == 0 or atom_list[i][2] == 1 and atom_list[j][2] == 2:
                        chk_list.append((abs(dx) + abs(dy), i, j))
        print('#{} {}'.format(tc, stack()))


sol()
