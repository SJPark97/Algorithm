import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')

    # 색칠할 영역 설정
    territory = [[0 for _ in range(10)] for _ in range(10)]

    # 박스 개수를 받아서 반복문
    boxs = int(input())
    for box_case in range(boxs):
        r1, c1, r2, c2, color = map(int, input().split())

        # 영역에 색칠
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if territory[i][j] == color or territory[i][j] == 0:
                    territory[i][j] = color
                else:
                    territory[i][j] += color
    
    # 보라색 영역의 개수 출력
    result = 0
    for _ in range(10):
        for cnt in range(3):
            result += territory[_].count(cnt)
    print(100 - result)



