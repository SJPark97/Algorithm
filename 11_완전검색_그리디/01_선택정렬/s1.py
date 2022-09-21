def selectionsort(a, s):
    if s == n - 1:
        return
    min_index = s
    for i in range(s, n):
        if a[min_index] > a[i]:
            min_index = i
    a[s], a[min_index] = a[min_index], a[s]
    selectionsort(a, s + 1)


A = [2, 4, 6, 1, 9, 8, 7, 0]
n = len(A)
selectionsort(A, 0)
print(A)
