def chk_list(num):
    cnt = 0
    for i in (0, 3):
        if num[i] == num[i + 1] == num[i + 2]:
            cnt += 1
        elif num[i] + 2 == num[i + 1] + 1 == num[i + 2]:
            cnt += 1
    if cnt == 2:
        return True
    return False


def chk(n, k):
    global answer
    if answer:
        return
    if n == k and chk_list(nums):
        answer = True
        return

    for i in range(n, k):
        nums[n], nums[i] = nums[i], nums[n]
        chk(n + 1, k)
        nums[n], nums[i] = nums[i], nums[n]


T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}', end=" ")
    nums = list(map(int, input()))
    answer = False
    chk(0, 6)
    print(answer)
