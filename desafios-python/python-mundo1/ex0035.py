'''Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se pode
ou não formar um triangulo'''

r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))

if r1 < r2 + r3 and r2 < r2 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
    