'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
...
def zero(): #your code here
def one(): #your code here
def two(): #your code here
def three(): #your code here
def four(): #your code here
def five(): #your code here
def six(): #your code here
def seven(): #your code here
def eight(): #your code here
def nine(): #your code here

def plus(): #your code here
def minus(): #your code here
def times(): #your code here
def divided_by(): #your code here
'''


def zero(a=None):
    return 0 if a is None else eval(str(0) + str(a[0]) + a[1])
def one(a=None):
    return 1 if a is None else eval(str(1) + str(a[0]) + a[1])
def two(a=None):
    return 2 if a is None else eval(str(2) + str(a[0]) + a[1])
def three(a=None):
    return 3 if a is None else eval(str(3) + str(a[0]) + a[1])
def four(a=None):
    return 4 if a is None else eval(str(4) + str(a[0]) + a[1])
def five(a=None):
    return 5 if a is None else eval(str(5) + str(a[0]) + a[1])
def six(a=None):
    return 6 if a is None else eval(str(6) + str(a[0]) + a[1])
def seven(a=None):
    return 7 if a is None else eval(str(7) + str(a[0]) + a[1])
def eight(a=None):
    return 8 if a is None else eval(str(8) + str(a[0]) + a[1])
def nine(a=None):
    return 9 if a is None else eval(str(9) + str(a[0]) + a[1])
def plus(a): return "+{}".format(a)
def minus(a): return "-{}".format(a)
def times(a): return "*{}".format(a)
def divided_by(a): return "/{}".format(a)

'''
def zero(arg=""):  return eval("0" + arg)
def one(arg=""):   return eval("1" + arg)
def two(arg=""):   return eval("2" + arg)
def three(arg=""): return eval("3" + arg)
def four(arg=""):  return eval("4" + arg)
def five(arg=""):  return eval("5" + arg)
def six(arg=""):   return eval("6" + arg)
def seven(arg=""): return eval("7" + arg)
def eight(arg=""): return eval("8" + arg)
def nine(arg=""):  return eval("9" + arg)

def plus(n):       return "+%s" % n
def minus(n):      return "-%s" % n
def times(n):      return "*%s" % n
def divided_by(n): return "/%s" % n
'''
print(one(divided_by(two())))
print(three(times(one())))
