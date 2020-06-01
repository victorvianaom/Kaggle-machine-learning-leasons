a = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']
for n in a: # the for loop mst specify a set of values to loop over
    print(n, end=', ')
print('\n')
palavra = 'inconstitucionaliscimamente'
for letra in palavra:
    print(letra, end='')
print('\n')

for i in range(4):
    print(i, end=' ')

palavra.upper()
print(palavra.upper())

print(sum([1 for letra in palavra if letra == 'i']))
print(sum([letra == 'i' for letra in palavra]))

print(any([False, True, False, False, False]))
print(any([False, False, False, False, False]))
print(any([letra == 'z' for letra in palavra]))