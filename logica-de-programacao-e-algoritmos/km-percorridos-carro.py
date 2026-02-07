# Escreva um programa que pergunte a quantidade de KM percorrido por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodado.

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM foram percorridos? '))

total = (dias * 60) + (km * 0.15)
print(f'Voce alugou o carro por {dias} dias e percorreu {km} KM.')
print(f'O valor total a pagar é de R${total:.2f}.')