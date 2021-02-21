#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo 
#retangulo, calcule e mostre o comprimento da hipotenusa
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co,ca)
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))
print('A hipotenusa vai medir {:.2f}'.format(hi))