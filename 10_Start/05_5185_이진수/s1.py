import sys

sys.stdin = open('input.txt')


def bit(num):
    result = ""
    for i in range(3, -1, -1):
        result += "1" if num & (1 << i) else "0"
    return result


n = int(input())
for t in range(n):
    l, nums = input().split()
    answer = ""
    for chk in nums:
        answer += bit(int(chk, 16))
    print(f'#{t + 1} {answer}')
