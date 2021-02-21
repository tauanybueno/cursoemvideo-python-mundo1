#crie um programa que leia um número real qualquer e mostre sua porção inteira
#ex: 6.127 --> 6
'''from math import trunc 
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))'''

num = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))
