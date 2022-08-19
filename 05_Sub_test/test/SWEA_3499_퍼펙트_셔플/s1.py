import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    n = int(input())
    h_n = n//2
    word = list(input().split())
    if n % 2:
        for i in range(h_n):
            print(word[i], word[i + h_n + 1], end=' ')
        print(word[h_n], end=' ')
    else:
        for i in range(h_n):
            print(word[i], word[i + h_n], end=' ')
    print()
    