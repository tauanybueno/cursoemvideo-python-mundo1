#crie um algoritmo que leia um número
#e mostre seu dobro, triplo e raiz quadrada 

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} é {}, o triplo é {} e a raíz quadarada é {:.3f}'.format(n,d,t,r))
