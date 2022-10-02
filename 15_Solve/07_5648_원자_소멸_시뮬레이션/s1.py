def sol():
    n = int(input())
    atom_list = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    answer = 0
    while atom_list and cnt < 4000:
        cnt += 1
        for i in range(len(atom_list)):
            atom_list[i][0] += dx[atom_list[i][2]]
            atom_list[i][1] += dy[atom_list[i][2]]
        delete_list = set()
        for i in range(len(atom_list) - 1):
            if i in delete_list:
                continue
            for j in range(i + 1, len(atom_list)):
                if (atom_list[i][0], atom_list[i][1]) == (atom_list[j][0], atom_list[j][1]):
                    delete_list.update([i, j])
        for index in sorted(list(delete_list))[::-1]:
            answer += atom_list[index][3]
            del atom_list[index]
    print(answer)


dx = [0, 0, -0.5, 0.5]
dy = [0.5, -0.5, 0, 0]
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=' ')
    sol()
