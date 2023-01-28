'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
...
def accum(s):
    # your code
'''


def accum(s):
    i = 1
    str = []
    for elem in s:
        str.append(elem.upper() + elem.lower()*(i-1))
        i += 1
    return "-".join(str)


print(accum("RqaEzty"))
'''
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
'''