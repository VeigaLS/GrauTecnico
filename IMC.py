peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = altura * altura / peso
if imc < 20:
    print("Abaixo do peso")
elif imc <= 25:
    print("Peso normal")
elif imc <= 30:
    print("Acima do peso")
else:
    print("Obeso")