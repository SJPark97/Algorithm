import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    A, B = input().split()
    # A의 길이에서 B의 길이 -1 만큼을 B가 들어간 횟수만큼 곱해서 빼기
    print(len(A) - A.count(B)*(len(B)-1))
