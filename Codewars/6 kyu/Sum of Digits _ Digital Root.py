'''
DESCRIPTION:
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
...
def digital_root(n):
    # ...
'''
def digital_root(n):
    li = sum([int(n) for n in str(n)])
    while len(str(li)) > 1:
        li = sum([int(i) for i in str(li)])
    return li

print(digital_root(493193))

'''
def digital_root(n):
    while n>9:
        n=sum(map(int,str(n)))
    return n
'''
'''
def digital_root(n):
    return n if n < 10 else digital_root(sum([int(c) for c in str(n)]))
'''
'''
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
'''
'''
def digital_root(num, res=0):
    if not num:
        return res
    res += num % 10
    num //= 10
    return digital_root(num, res)
'''