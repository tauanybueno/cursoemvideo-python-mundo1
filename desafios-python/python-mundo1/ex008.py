#escreva um programa que leia um valor em metros e o exiba
#convertido em centímetros e milímetros

m = float(input('Digite o valor em metros: '))
c = m * 100
mili = m * 1000
print('O valor em centimetros é {:.0f}cm e em milímetros {:.0f}mm'.format(c,mili))