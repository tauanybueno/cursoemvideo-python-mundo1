'''Faça um prograa que leia uma frase pelo teclado e mostre:
quantas vezes aparece a letra A
em que posição ela aparece a primeira vez
em que posição ela aparece a última vez'''

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))
