'''faça um programa que leia um ano qualquer e mostre se ele é bissexto'''

ano = int(input('Digite um ano: '))

#dívisivel por 4
#não ser multiplo de 100
#ser multiplo de 400

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))