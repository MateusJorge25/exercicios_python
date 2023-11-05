
v = int(input("Insira a velocidade:"))


if v > 110:
    print("Você foi multado")

    multa = (v - 110) * 5

    print ("vai ter que pagar:", multa)

elif v <= 110:
    print("esta na velocidade")