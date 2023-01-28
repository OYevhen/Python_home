'''
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
...
def count(string):
    # The function code should be here
    return {}
'''

def count(string):
    k = {}
    for i in string:
        if i in k:
            k[i] += 1
        else:
            k[i] = 1
    return k

print(count("cccaba"))

'''
def count(string):
    print({i: string.count(i) for i in string})
'''

