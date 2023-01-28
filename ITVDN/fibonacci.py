# fibs = [1, 1]
# nums = 10
# for i in range(nums - 2):
#     fibs.append(fibs[i] + fibs[i+1])
# print(fibs)

def fibonacci(count):
    first, second = 0, 1
    for _ in range(count):
        yield second
        first, second = second, first + second

count = 10
for fib in fibonacci(count):
        print(fib)