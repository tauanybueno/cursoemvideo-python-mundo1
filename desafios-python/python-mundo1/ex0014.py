#escreve um programa que converta uma temepratura digitaca em C para F 
#F = C X 1.8 + 32

cel = float(input('Digite a temperatura em C: '))
f = cel * 1.8 + 32
print('A temperatura {} em Celsius equivale a {} em Fahrenheit'.format(cel,f))