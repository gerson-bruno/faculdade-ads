# Traduza as afirmações a seguir para condicionais em Python:
# Se a idade é maior que 60, mostre 'Você tem direito a aposentadoria'

idade = int(input("Digite sua idade: "))
if idade > 60:
    print("Você tem direito a aposentadoria")
else:
    print("Você não tem direito a aposentadoria")

#Se dano é maior que 10 e escudo é igual a 0, escreva: 'Você está morto!'
dano = int(input("Digite o dano: "))
escudo = int(input("Digite o escudo: "))
if dano > 10 and escudo == 0:
    print("Você está morto!")
else:
    print("Você ainda está vivo!")

#Exemplo de como fazer sem deixar o usuário digitar, também funciona para a expressão acima

dano = 13
escudo = 0
if dano > 10 and escudo == 0:
    print("Você está morto!")

#Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for verdadeira, mostre 'Você escapou!'
norte = True
sul = False
leste = False
oeste = False
if norte or sul or leste or oeste == True:
    print("Você escapou!")
# Foi utilizado o operador OR para verificar se pelo menos uma das variáveis booleanas é verdadeira, caso fosse utilizando o operador AND, todas as variáveis precisariam ser verdadeiras para que a expressão retornasse True
