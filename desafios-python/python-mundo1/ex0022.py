'''Crie um programa que leia o nome completo de uma pessoa e mostre:
o nome com todas as letras maiúsculas
o nome com todas minúsculas
quantas letras ao todo (sem considerar espaços)
quantas letras tem o primeiro nome '''

nome = str(input('Digite o seu nome completo: ')).strip()
#elimina os espaços antes e depois 

print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
nome.find(' ')
#encontra o primeiro espaço de 0 até o primeiro espaço
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()
#cria uma lista com os nomes
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))


