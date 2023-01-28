'''
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
...
def solution(s):
    pass
'''
def solution(s):
    s2 = ""
    for elem in s:
        if elem == elem.upper():
            s2 += " "+elem
        else:
            s2 += elem
    return s2
'''
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
'''
'''
def solution(s):
    return ''.join(i if i.islower() else ' ' + i for i in s)
'''


text = "helloWorld"
text2 = "camelCase"
text3 = "breakCamelCase"

print(solution(text3))
