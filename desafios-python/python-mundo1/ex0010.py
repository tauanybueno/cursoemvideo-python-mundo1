#crie um programa que leia quanto dinheiro ela tem na carteira 
# e mostre quantos dólares ela pode comprar 
# 1.00 = 3,27 

n = float(input('Digite quanto você tem na carteira: R$'))
d = n / 3.27
print('Com R${:.2f} reais você pode comprar U${:.2f} dólares'.format(n,d))