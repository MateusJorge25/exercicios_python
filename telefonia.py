import math

m = int(input("Quantos minutos você falou:"))

if m < 200:
    
    custo = (m - 200) * 0.20

    print("1 Seu custo sera de R$:", custo)

if m <= 400:

    custo2 = (m - 200) * 0.18

    print("2 Seu custo sera de R$:", math.floor(custo2))

if m > 400:

    custo3 = (m - 400) * 0.15

    print("3 Seu custo sera de R$:", custo3)