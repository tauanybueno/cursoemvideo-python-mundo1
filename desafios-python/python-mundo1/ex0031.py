'''desenvolva um programa que pergunte a distancia de uma viagem em km
calcule o preço da passagem cobrando 0,50 por km para viagens ate 200km
e 0,45 para viagens mais longas'''

km = float(input('Qual a distância da sua viagem em KM? '))
op1 = km * 0.50
op2 = km * 0.45

if km <= 200:
    print('O valor da sua viagem será: R${:.2f}'.format(op1))
else:
    print('O valor da sua viagem será: R${:.2f}'.format(op2))

