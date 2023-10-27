
num1 = int(input("Digite a primeira nota: "))

num2 = int(input("Digite a segunda nota: "))

num3 = int(input("Digite a terceira nota: "))

num4 = int(input("Digite a quarta nota: "))

media = (num1 + num2 + num3 + num4) / 4

print(media)

if (media >=6):
    print("passou")
                                # if feito por conta para mostrar se o aluno passou ou reprovou
else:
    print("reprovou")
