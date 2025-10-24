import numpy as np
for n in range(1, 1000):
    s  = (np.base_repr(n, base= 3))[::]
    if n % 2 == 0:
        s = '2' + s
        s += str(np.base_repr(int(s[-1], 3) * 2, base= 3))
    else:
        s += '2'
        s = str(np.base_repr(int(s[0], 3) * 2, base= 3)) + s
    if int(s, 3) > 100:
        print(int(s, 3))
        break