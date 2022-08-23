# from itertools import permutations, combinations


def combinations(arr, start, total):
    global cnt
    cnt += 1
    if total > 10:
        return
    if total == 10:
        print(arr)
        return
    for i in range(start, len(numbers)):
        arr.append(numbers[i])
        combinations(arr, i + 1, total + numbers[i])
        arr.pop()


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
cnt = 0
combinations([], 0, total)
print(cnt)

def powerset(arr, depth, total):
    # 가지치기(pruning): 합이 10 초과면 더 진행할 필요가 없다.
    if total > 10:
        return

    # 전체 원소의 개수만큼 재귀가 진행됐다면 종료
    if depth == len(numbers):
        # 원소의 합이 10이라면 해당 부분집합 출력
        if total == 10:
            print(arr)
        return

    # 1) 현재 원소를 뽑고 다음 재귀로 진행하는 경우
    powerset(arr + [numbers[depth]], depth + 1, total + numbers[depth])

    # 2) 현재 원소를 뽑지 않고 다음 재귀로 진행하는 경우
    powerset(arr, depth + 1, total)


numbers = list(range(1, 11))
powerset([], 0, 0)
