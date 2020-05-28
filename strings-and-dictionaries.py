string = """firstt line
second one
the third"""

print(string)
print('A' == 'a')

palavra = 'Palavra'
print([letra + '!' for letra in palavra])

# palavra[0] = 'B' , str object does not support item assignment
print(palavra.index('ra'))
print(len(palavra), palavra.startswith('Pal'), palavra.startswith('pal')) 

frase = 'isso aqui e uma frase de oito palavras'
print(frase.split(), len(frase.split()))
print('/'.join(['30', '11', '1994']))