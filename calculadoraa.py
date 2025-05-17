option = 0
result = 0.0
while option != "0":
    print(" -+/*CALCULADORA-+/*")
    num1 = float(input("Primeira célula: "))
    print("_________________")
    option = input("Escolha a operação:\n+ Somar \n- Subtrair \n* Multiplicar \n/ Dividir \n0 Sair\nEscolha^^^^: ")
    print("_________________")
    if option == '0':
        print("Saindo...")
        break
    num2 = float(input("Segunda célula: "))
    if option == '+':
        result = num1 + num2
        print("_________________")
        print(f"Resultado: {num1} + {num2} = {result}")
    elif option == '-':
        result = num1 - num2
        print("_________________")
        print(f"Resultado: {num1} - {num2} = {result}")
    elif option == '*':
        result = num1 * num2
        print("_________________")
        print(f"Resultado: {num1} * {num2} = {result}")
    elif option == '/':
        if num2 != 0:
            result = num1 / num2
            print("_________________")
            print(f"Resultado: {num1} / {num2} = {result}")
        else:
            print("Ta tentando dividir por zero???")
    else:
        print("Operação inválida.")