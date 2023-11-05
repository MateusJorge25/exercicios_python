
peso = int(input("Digite o peso do peixe:"))


if peso > 50:
    excesso = peso-50
    multa = excesso*4


    print("Kg em excesso:", excesso)

    print("Valor da multa:", multa)


else:
    print("Esta nas normas")