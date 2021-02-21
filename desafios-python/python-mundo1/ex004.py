#faça um programa que leia algo pelo teclado e mostre na tela
#seu tipo primitivo e todas as possiveis informações sobre aquilo

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
#será str porque todo input retorna string a não ser 
#que coloque antes int, bool, float
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanúmerico?', a.isalnum())
print('Esta em maiúcula?', a.isupper())
print('Esta em minúscula?', a.islower())
print('Está capitalizada?', a.istitle())

