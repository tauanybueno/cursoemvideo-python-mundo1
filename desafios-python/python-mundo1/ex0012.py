#faça um algoritmo que leia o preço de um produto 
# e mostre seu novo preço com 5% de desconto

pre = float(input('Digite o preço do produto: R$'))
desc = pre * (5/100)
final = pre - desc
print('O produto custava R${:.2f} e teve 5% de desconto. O novo valor é R${:.2f}'.format(pre, final))