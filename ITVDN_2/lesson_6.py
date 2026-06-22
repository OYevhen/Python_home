# print(print.__doc__)

# def foo():
#     global var
#     var = '321'
#     print(var)

# var = '123'
# foo()
# print(var)

###

# def summator(a, b):
#     sum = 0
#     for i in range (a, b + 1):
#         sum += i
#         print(sum)
#     return sum

# print(summator(1, 5))

###

# frase = 'abccba'
# def polindrome(frase):
#     if frase == frase[::-1]:
#         return True
#     else:
#         return False

# def polindrome2(frase):
#     if list(frase) == list(reversed(frase)):
#         return True
#     else:
#         return False
    
# print(polindrome2(frase))

###

number_of_steps = 3
possible_ways = 0

def count_ways(number_of_steps):
    global possible_ways
    for _ in range(1, number_of_steps + 1):
        if _ < number_of_steps:
            possible_ways += 1
        if _ + 1 < number_of_steps:
            possible_ways += 1
    return possible_ways

print(count_ways(number_of_steps))