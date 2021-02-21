#desenvolva um programa que leia as duas notas de um aluno
#calcule e mostre a média 

n1 = float(input('Digite a 1 nota do aluno: '))
n2 = float(input('Digite a 2 nota do aluno: '))
s = n1 + n2 
m = s / 2
print('A média das notas do aluno é: {:.1f}'.format(m))