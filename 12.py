#максимальная сумма цифр
from itertools import permutations

def f(s = str()):
    s.replace("42", "51")
    s.replace("32", "61")
    return sum(int(x) for x in s)

symbols = "111122223333" # все символы из задачи
c = 0
for x in permutations(symbols):
    c1 = f(''.join(x))
    c = max(c, c1)
print(c)

# простой но не эфективный перебор вариантов, 
# при большом колличестве данных может быть длительная обработка