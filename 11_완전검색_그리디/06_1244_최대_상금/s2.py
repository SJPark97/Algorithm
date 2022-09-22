def sol():
    nums, t = input().split()
    nums = list(map(int, list(nums)))[::-1]
    cnt_list = [0] * 10
    signal = True
    for i in nums:
        cnt_list[i] += 1
        if cnt_list[i] == 2:
            signal = False
            break
    t = int(t)
    l = len(nums) - 1
    while t > 0:
        if nums == sorted(nums):
            break
        max_num = max(nums[:l + 1])
        max_index = nums.index(max_num)
        if max_index == l:
            l -= 1
            continue
        max_cnt = nums[:l + 1].count(max_num)
        if max_cnt > 1 and t > 1:
            if max_cnt > t:
                nums = nums[:l + 1 - t] + sorted(nums[l + 1 - t:l + 1])[::-1] + nums[l + 1:]
            else:
                nums = nums[:l + 1 - max_cnt] + sorted(nums[l + 1 - max_cnt:l + 1])[::-1] + nums[l + 1:]
        nums[l], nums[max_index] = nums[max_index], nums[l]
        t -= 1
        l -= 1
        if l == 0:
            break
    if t % 2 and signal:
        nums[0], nums[1] = nums[1], nums[0]
    print(*nums[::-1], sep="")


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
