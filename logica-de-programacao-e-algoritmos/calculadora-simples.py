# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual a operação ele deseja realizar: adição (+), subtração (-), multiplicação (*) e divisão (/). Exiba na tela o resultado da operação escolhida.

n1 = int(input("Digite o primeiro número: "))
op = input("Digite a operação desejada (+, -, *, /): ")
n2 = int(input("Digite o segundo número: "))


if op == "+":
    resultado = n1 + n2
    print(f"O resultado da adição é: {resultado}")
elif op == "-":
    resultado = n1 - n2
    print(f"O resultado da subtração é: {resultado}")
elif op == "*":
    resultado = n1 * n2
    print(f"O resultado da multiplicação é: {resultado}")
elif op == "/":
    if n2 != 0:
        resultado = n1 / n2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro, não é permitido divisão por zero!")












