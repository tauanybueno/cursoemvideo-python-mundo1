'''Escreva um desafio que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobir qual foi o número escolhido. O programa deverá escrever
na tela se o usuário perdeu ou venceu'''

#gerar o número aleatório
import random
from time import sleep
computador = (random.randint(0,5))
#print(num)

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
sleep(2)

#perguntar ao usuário
jogador = int(input('Qual número você acha que foi escolhido? '))

print('PROCESSANDO...')
sleep(2)

#condição
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('VOCÊ ERROU! O número que eu pensei foi {}'.format(computador))