#русификация консоли windows
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from itertools import*

tab = '24 146 56 1267 36 23457 46'.split() 
pic = 'аб ав бв вг вд ве де ге ек кг'.split() 
print(*range(1, 8)) 
for var in permutations('абвгдек'): 
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print(*var)