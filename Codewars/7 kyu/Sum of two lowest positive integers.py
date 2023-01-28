'''
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
...
def sum_two_smallest_numbers(numbers):
    #your code here
'''


def sum_two_smallest_numbers(numbers):
    nums = []
    for i in numbers:
        if i < 0 or type(i) == float:
            continue
        else:
            nums.append(i)
    nums.sort()
    return nums[0] + nums[1]


arr = [-2, 19, 5, 42, 2, 77, 0.3, -1]
print(sum_two_smallest_numbers(arr))
'''
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
'''