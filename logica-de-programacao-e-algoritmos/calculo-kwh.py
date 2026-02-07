#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação (R para residencial, I para industrial e C para comércio).
# Residencial: até 500 kWh R$ 0,40 por kWh acima de 500 kWh R$ 0,65 por kWh
# Industrial: até 5000 kWh R$ 0,55 por kWh acima de 5000 kWh R$ 0,60 por kWh
# Comércio: até 1000 kWh R$ 0,55 por kWh acima de 1000 kWh R$ 0,60 por kWh

kwh = float(input("Quantos kWh? "))
instalacao = input("Qual o tipo de instalação: R, I ou C? ")

if instalacao == "R":
    if kwh > 500:
        print("Valor a pagar: R$", kwh * 0.65)
    else:
        print("Valor a pagar: R$ ", kwh * 0.40)
elif instalacao == "I":
    if kwh > 5000:
        print("Valor a pagar: R$ ", kwh * 0.60)
    else:
        print("Valor a pagar: R$ ", kwh * 0.55)
elif instalacao == "C":
    if kwh > 1000:
        print("Valor a pagar: R$ ", kwh * 0.60)
    else:
        print("Valor a pagar: R$ ", kwh * 0.55)
