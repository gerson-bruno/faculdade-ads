#Traduza as afirmações a seguir para condicionais em Python:
# a - Se ano é divisível por 4, escreva: "O ano é bissexto". Caso contrário, escreva: "O ano não é bissexto".
# b- Se ambas as variáveis booleanas cima e baixo forem verdadeiras, escreva: "Decida-se!". Caso contrário, escreva: "Você escolheu um caminho!".

# Exercício A
ano = int(input("Digite um ano: "))
if (ano % 4 == 0):
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")

# Exercício B
cima = True
baixo = True
if (cima and baixo == True):
    print("Decida-se!")
else:
    print("Você escolheu um caminho!")
