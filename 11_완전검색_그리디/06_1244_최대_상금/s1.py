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
    past_num = -1
    while t > 0:
        max_index = nums.index(max(nums[:l + 1]))
        if max_index != l:
            nums[l], nums[max_index] = nums[max_index], nums[l]
            if past_num == nums[l] and nums[max_index] < nums[max_index - 1]:
                nums[max_index], nums[max_index - 1] = nums[max_index - 1], nums[max_index]
            past_num = nums[l]
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
