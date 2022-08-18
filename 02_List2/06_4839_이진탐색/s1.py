import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    # input 정보 받아오기, A, B 탐색 초기값 설정
    r, A_p, B_p = map(int, input().split())
    list_i = [1, 1]     # 책의 시작 페이지
    list_r = [r, r]     # 책의 마지막 페이지
    list_p = [A_p, B_p] # 찾아야 되는 페이지
    list_cnt = [0, 0]   # 탐색 횟수

    # 탐색 시작
    for case in range(2):
        while True:
            c = int((list_i[case]+list_r[case])/2)
            list_cnt[case] += 1
            
            # 탐색한 페이지가 찾아야 되는 페이지보다 클때
            if c > list_p[case]:
                list_r[case] = c - 1
                
            # 탐색한 페이지가 찾아야 되는 페이지보다 작을때
            elif c < list_p[case]:
                list_i[case] = c + 1
                
            # 페이지를 찾았을 때
            else:
                break
    
    # A와 B가 탐색한 횟수 비교
    if list_cnt[0] < list_cnt[1]:
        print('A')
    elif list_cnt[0] > list_cnt[1]:
        print('B')
    else:
        print(0)

