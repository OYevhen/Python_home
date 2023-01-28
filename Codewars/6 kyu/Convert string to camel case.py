'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
...
def to_camel_case(text):
    #your code here
'''
def to_camel_case(text):
    text2 = ""
    flag = False
    for i in text:
        if i == "-" or i == "_":
            flag = True
        elif flag is True:
            text2 += i.upper()
            flag = False
        else:
            text2 += i
    return text2

'''
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
'''


print(to_camel_case("The_Stealth_Warrior"))
