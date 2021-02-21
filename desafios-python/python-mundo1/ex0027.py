'''Faça um programa que leia um nome e mostre o primeiro
e o ultimo nome separadamente'''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split() #vai dividir o nome em pedaços separados por espaços 
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome) - 1]))