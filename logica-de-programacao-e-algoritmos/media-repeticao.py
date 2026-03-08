soma = 0
cont = 1
while (cont <= 5):
    x = float(input(f'Digite a {cont}ª nota: '))
    soma += x
    cont += 1
media = soma / 5
print(f'Média final é de {media}!')
if(media >= 7):
    print('Aprovado')
else:
    print('Reprovado')