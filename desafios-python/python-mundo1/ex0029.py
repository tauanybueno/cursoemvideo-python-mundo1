'''Escreva um computador que leia a velocidade de um carro. Se ele ultrapassar a velocidade de
80km/h mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por
cada km acima do limite'''

velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7.00 
    print('Você recebeu uma multa de R${:.2f} por estar acima do limite de 80Km/h'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança')