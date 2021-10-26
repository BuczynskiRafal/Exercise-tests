# def factorial(n):
#     if n == 0:
#         return 1
#     number = 1
#     for i in range(1, n+1):
#         number = number * i
#     return number

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(10))