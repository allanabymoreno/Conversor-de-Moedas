real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.16 #cotação do dolar no dia 07/08/22
print('Com R${:.2f} você pode comprar U${:.2f}'. format(real, dolar))