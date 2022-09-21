def sol():
    num = list(map(int, list(input())))
    nums = [0] * 12
    cnt = 0
    for n in num:
        if nums[n] == 2:
            cnt += 1
            if cnt == 2:
                result.append('True')
                return
            nums[n] = 0
        else:
            nums[n] += 1
    for i in range(10):
        if nums[i] == 2 and nums[i+1] == 2 and nums[i+2] == 2:
            result.append('True')
            return
        elif nums[i] == 1 and nums[i+1] > 0 and nums[i+2] > 0:
            cnt += 1
            nums[i+1] -= 1
            nums[i+2] -= 1
            if cnt == 2:
                result.append('True')
                return
    result.append('False')
    return


result = []
for test_case in range(1, int(input()) + 1):
    sol()
print(*result, sep="\n")
