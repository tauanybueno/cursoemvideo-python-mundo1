#faça um programa que leia a largura e a altura de uma parede
#em metros, calcule sua área e a quantidade de tinta necessária 
#para pintá-la, sabendo que cada litro de tinta pinta uma área de 2mˆ2

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt 
tinta = area / 2 
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(larg,alt, area))
print('Para pintar uma parede de área {:.3f} será necessário {:.3f}L3 de tinta'.format(area, tinta))