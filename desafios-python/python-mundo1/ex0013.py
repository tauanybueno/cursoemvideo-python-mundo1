#faça um algoritmo que leia o sálario de um funcionário 
#e mostre seu novo salário com 15% de aumento 

sal = float(input('Digite o seu salário: '))
aument = sal * (15/100)
final = sal + aument 
print('O salário era de R${:.3f} e com um aumento de 15% passou para R${:.3f}'.format(sal,final))