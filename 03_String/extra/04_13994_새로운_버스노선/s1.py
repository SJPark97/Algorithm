import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    N = int(input())
    all_bus_stop = [range(1, 1001)]

    for case in range(N):
        bus_type, start, end = map(int, input().split())
        if bus_type == 1:
            station = [start, range(start, end + 1), end]
        elif bus_type == 2:
            station = [start, range(start, end + 1, 2), end]
        else:
            if start % 2:
                break
            elif:
                station = [start, range(start, end + 1, 2), end]

list_a = [1, 2, 3, 4]
list_a[start:end+1] += 1

