#Faça um algorítmo que receba 3 valores, representando os lados de um triângulo fornecidos pelo usuário. Verifique se os valores formam um triangulo e classifique o triângulo como equilátero, isósceles ou escaleno.
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes
# Triângulo: soma de dois lados deve ser maior que o terceiro lado e todos os lados devem ser maiores que zero.

l1 = int(input("Digite o comprimento do primeiro lado: "))
l2 = int(input("Digite o comprimento do segundo lado: "))
l3 = int(input("Digite o comprimento do terceiro lado: "))

if ((l1 > 0 and l2 > 0 and l3 > 0) and (l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1)):
    #Se chegou até aqui é porque o triângulo é válido.
    if (l1 != l2 and l1 != l3 and l2 != l3):
        print("Triângulo escaleno")
    elif (l1 == l2 and l1 == l3 and l2 == l3):
        print("Triângulo equilátero")
    else:
        print("Triângulo isósceles")
else:
    print("Não é um triângulo")
