def tower_builder(n_floors):
    floor = 2
    tree = []
    tree.append("*".center(n_floors*2-1))
    for i in range(n_floors-1):
        tree.append(("*"*(floor*2-1)).center(n_floors*2-1))
        floor += 1

    return tree


print('\n'.join(tower_builder(6)))

'''
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
'''