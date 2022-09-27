def sol():
    def sort(num, start, end):
        i, j = start, end
        while i <= j:
            while i <= j and num[i] <= num[start]:
                i += 1
            while i <= j and num[j] >= num[start]:
                j -= 1
            if i < j:
                num[i], num[j] = num[j], num[i]
        num[start], num[j] = num[j], num[start]
        return j

    def quick_sort(num, start, end):
        if start < end:
            middle = sort(num, start, end)
            quick_sort(num, start, middle - 1)
            quick_sort(num, middle + 1, end)
        return

    n = int(input())
    nums = list(map(int, input().split()))
    quick_sort(nums, 0, len(nums) - 1)
    print(nums[n//2])


for test_case in range(1, int(input())+1):
    print(f"#{test_case}", end=" ")
    sol()
