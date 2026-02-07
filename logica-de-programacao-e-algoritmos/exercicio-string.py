# Crie uma variavel de string que recebe uma frase qualquer. Crie uma segunda variável, agora contendo a metade da string digitada. imprima na tela somente os dois últimos caracteres da segunda variavel.

frase = input('Digite uma frase qualquer: ')
tamanho = len(frase)
metade = frase[:int(tamanho/2)]
print(metade[-2:])