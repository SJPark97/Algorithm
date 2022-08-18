# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-2) + fibo(n-1)
#
# print(fibo(int(input())))

def fibo(n):
    if len(memo) <= n:
        memo.append(fibo(n - 1) + fibo(n - 2))
    return memo[n]


memo = [0, 1]

print(fibo(int(input())))

