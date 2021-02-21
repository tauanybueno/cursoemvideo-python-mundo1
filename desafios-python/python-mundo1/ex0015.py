#escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado 
#calcule o preço a pagar sabendo que o carro custa 60 por dia e 0.15 por km rodado

km = float(input('Quantos quilometros foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
pagar = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pagar))