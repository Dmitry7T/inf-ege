#максимальная сумма цифр

# эксперементальный вариант для смелых
# перебор с использованием GPU, кратное ускорение процеса ценой краша

import cupy as cp
import numpy as np
from itertools import permutations

def f_gpu_batch(permutations_array):
    result = cp.zeros(len(permutations_array), dtype=cp.int32)
    
    for i in range(len(permutations_array)):
        s = permutations_array[i]
        total = 0
        for char in s:
            total += int(char)
        result[i] = total
    
    return result

def gpu_permutations_search(symbols):
    all_perms = list(permutations(symbols))
    strings = [''.join(p) for p in all_perms]
    strings_gpu = cp.array(strings, dtype=cp.str_)
    results_gpu = f_gpu_batch(strings_gpu)
    max_value = cp.max(results_gpu)
    
    return max_value.get()

symbols = '2' * 20 + '3' * 15 + '4' * 10
result = gpu_permutations_search(symbols)
print(f"Максимум: {result}")

# ошибка MemoryError означает что комп не потянул