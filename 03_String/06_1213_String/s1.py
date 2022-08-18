import sys

sys.stdin = open("input.txt", "r", encoding="utf-8")

for _ in range(10):
    print(f'#{input()}', end=' ')
    check = input()
    word = input()
    print(word.count(check))