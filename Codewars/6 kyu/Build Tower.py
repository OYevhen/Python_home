'''
Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ",
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ",
  "    ***    ",
  "   *****   ",
  "  *******  ",
  " ********* ",
  "***********"
]
...
def tower_builder(n_floors):
    # build here
'''
def tower_builder(n_floors):
    for i in range(n_floors):
        print(" "*(n_floors-i), "*"*i, "*", "*"*i, " "*(n_floors-i), sep="")
    return ""

'''
def tower_builder(n):
    return [('*' * i).center(n * 2 - 1) for i in range(1, 2 * n + 1, 2)]
'''

'''
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
'''

print(tower_builder(6))
