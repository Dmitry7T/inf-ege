from itertools import*
def f(x, y, z, w):
    return x and y and z and w
for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat = 7):
    table = [(1, a1, a2, 1), (a3, a4, a5, 1), (1, a6, 1, a7)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(*p, sep='')