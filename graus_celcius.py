import math  # Usando a função de matematica do python para arredondar a resposta


f = int(input("Digite os graus em fahrenheit:"))

c = 5 * ((f-32)/9)

print("A temperatura em graus Celcius é:", math.floor(c))


if (c >= 30):
    print("Esta muito quente!!")

else:
    print("Esta agradavel!!")