'''
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
...
def valid_parentheses(string):
    #your code here
    return False
'''
def valid_parentheses(string):
    flag = 0

    for i in string:
        if i == "(":
            flag += 1
        if i == ")":
            flag -= 1
            if flag < 0:
                return False
    return flag == 0

print(valid_parentheses("hi())("))

'''
def valid_parentheses(string):
    new = ''.join([i for i in string if i in '()'])
    while '()' in new:
        new = new.replace('()', '')
    return len(new) == 0
'''