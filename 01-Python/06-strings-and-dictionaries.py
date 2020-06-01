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
print('👏'.join(['antes da palma', 'depois da palma']))
palma = '👏'
print(palma)

s = "eu vou pra {0} da minha {1}, por que na {0} da minha {1} tem gente que mora na {0}".format('casa', 'mae')
print(s)
s = 'hoje {} vou {} uma {} muito {}'.format('eu', 'fazer', 'coisa', 'massa')
print(s)

dic = {
    'one': 1,
    'two': 2,
    'three': 3,
}
print(dic)
print(dic['one'])
print([n for n in dic])
dic['eleven'] = 11
print([n for n in dic])

nomes = ['Victor', 'Sarah', 'Ana Clara', 'Helder']
dic = {nome: nome[0] for nome in nomes}
print(dic)
for i in dic:
    print('{} = {}'.format(i, dic[i]))
print(dic.values(), type(dic.values()))
print(dic.keys(), type(dic.keys()))
print(dic.items(), type(dic.items()))
print(type(1), type('um'), type(False), type(1.1))

for name, initial in dic.items(): ########################### this is so much important ######################
    print('{} begins with {}'.format(name, initial)) ######## to iterate over dictionaries ###################

str()
int()
float()
bool()
list()
tuple()
dict()

print(str('12345').isnumeric())
print('eu sou muito lindoo'.find('lindo'), 'b'.find('a'))