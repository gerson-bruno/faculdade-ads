preco = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o percentual de desconto (0-100%): '))

desconto = preco * (percentual / 100)
novo_preco = preco - desconto

print(f'O preço do produto é {preco} e o desconto foi de {percentual}%')
print(f'O valor calculado de desconto: {desconto}.')
print(f'O valor final do produto é: {novo_preco}')
