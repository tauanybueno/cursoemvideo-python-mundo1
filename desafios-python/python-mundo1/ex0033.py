'''faça um programa que leia 3 números e mostre qual é o maior e qual é o menor'''

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

#achar o maior número
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

#achando o menor
menor = a 
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

print('Entre os números {}, {} e {}:'.format(a,b,c))
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))