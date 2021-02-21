'''escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento
Para salários > 1.250 aumento de 10%
para salários inferiores ou iguais aumento de 15%'''

sal = float(input('Digite o salário do funcionário: R$'))

if sal <= 1250:
    novo = sal + (sal * 15/100)
    print('O salário com um aumento de 15% é {}'.format(novo))
else:
    novo = sal + (sal * 101/100)
    print('O salário com um aumento de 10% é {}'.format(novo))