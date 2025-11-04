import itertools

cods = '1110 011 1001 1111 0001 0000 110 0011 0100'
for length in range(5):
    for bits in itertools.product('01', repeat= length):
        candidate = ''.join(bits)
        if candidate not in cods:
            print(candidate)
            break