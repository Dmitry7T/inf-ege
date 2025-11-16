import numpy as np

x = 8 ** 560 - 2 ** 234 + 56
s = str(np.base_repr(x, 2))
c = s.count('0')

print(c)