def a(x, y, t, dessert_list):
    for _ in range(t):
        x, y = x + dx[0], y + dy[0]
        if 0 <= x < n and 0 <= y < n:
            dessert_list.append((x, y))
        else:
            return False
    return True


def b():
    x = 2
    y = 2
    dessert_list = []
    if a(x, y, 2, dessert_list):
        print(x, y)
    print(dessert_list)
    return


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = 4
b()
