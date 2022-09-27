def sol():
    def merge(left, right):
        i = j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result + left[i:] + right[j:]

    def merge_sort(num):
        nonlocal cnt
        if len(num) <= 1:
            return num

        left = merge_sort(num[:len(num) // 2])
        right = merge_sort(num[len(num) // 2:])
        if left[-1] > right[-1]:
            cnt += 1
        return merge(left, right)

    n = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    print(merge_sort(nums)[n // 2], cnt)


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=" ")
    sol()
