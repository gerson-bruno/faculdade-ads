# x = 1;
# while (x  <= 10):
 #   print(x)
  #  x = x + 1

inicio = int(input('Qual o número inicial? '));
fim = int(input('Qual o número final? '));

x = inicio
while (x <= fim):
    if (x % 2 == 0):
        print(x)
    x = x + 1

