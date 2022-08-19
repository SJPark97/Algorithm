def solution(places):
    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for place in places:
        result = 1
        for i in range(5):
            if result == 0:
                break
            for j in range(5):
                if result == 0:
                    break
                if place[i][j] == 'P':
                    for n1 in range(4):
                        mx1 = i + dx[n1]
                        my1 = j + dy[n1]
                        if 0 <= mx1 < 5 and 0 <= my1 < 5:
                            if place[mx1][my1] == 'P':
                                result = 0
                                break
                            elif place[mx1][my1] == 'O':
                                for n2 in range(4):
                                    mx2 = mx1 + dx[n2]
                                    my2 = my1 + dy[n2]
                                    if 0 <= mx2 < 5 and 0 <= my2 < 5:
                                        if mx2 == i and my2 == j:
                                            pass
                                        else:
                                            if place[mx2][my2] == 'P':
                                                result = 0
                                                break
        answer.append(result)
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
         ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
         ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
         ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
         ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))