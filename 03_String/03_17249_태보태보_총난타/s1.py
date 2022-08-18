punch = input()

punch_cnt = 0

for cnt in punch:
    if cnt == '@':
        punch_cnt += 1
    elif cnt == '(':
        print(punch_cnt, end=' ')
        punch_cnt = 0

print(punch_cnt)


# left, right = input().split("0")
# print(left.count("@"), right.count("@"))