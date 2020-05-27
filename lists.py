a = ['gato', 'rato', 'pato', 'sapo', 'vaca']
print(a[0:2], a[-1], a[:2], a[2:])
print(a[1:-1])
print(a[-3:])

b = 'hoje em dia'
print(b[-3:])
a[:3] = ['cachorro', 'cavalo', 'cabra']
print(a)
print(len(a), len(b))
print(sorted(a), sorted(b))

c = [1, 17, 9, 30, 2, 4, 55, 56, 71, 8, 14]
print(sorted(c), sum(c), min(c), max(c))

x = 12
print(x.imag) # even a number is an object
y = 12 + 3j
print(y.imag)

print((11).bit_length)
print(x.bit_length) # access the method
print(x.bit_length()) # call the method
help(x.bit_length)

print(a)
print(a.append('animal')) #returns none
print(a)
print(a.pop()) #remove the last element and returns it
print(a)

print('nada' in a, 'vaca' in a, 'cabra' in a, 'vidro' in a)