# Entrada da opção de conversão
print("Conversor de Temperatura")
print("1 - Celsius(°C) para Fahrenheit(°F)")
print("2 - Celsius(°C) para Kelvin(K)")
print("3 - Fahrenheit(°F) para Celsius(°C)")
print("4 - Fahrenheit(°F) para Kelvin(K)")
print("5 - Kelvin(K) para Celsius(°C)")
print("6 - Kelvin(K) para Fahrenheit(°F)")
opcao = int(input("Qual a conversão desejada? (1-6): "))
if opcao < 1 or opcao > 6:
    print("Erro: Opção inválida! Entre 1 e 6 por favor!.")
    exit()
temperatura = float(input("Digite a temperatura a ser convertida: "))
if opcao == 1:
    resultado = (temperatura * 9/5) + 32
    print(f"{temperatura}°C = {resultado}°F")
elif opcao == 2:
    resultado = temperatura + 273.15
    print(f"{temperatura}°C = {resultado}K")
elif opcao == 3:
    resultado = (temperatura - 32) * 5/9
    print(f"{temperatura}°F = {resultado}°C")
elif opcao == 4:
    resultado = ((temperatura - 32) * 5/9) + 273.15
    print(f"{temperatura}°F = {resultado}K")
elif opcao == 5:
    resultado = temperatura - 273.15
    print(f"{temperatura}K = {resultado}°C")
elif opcao == 6:
    resultado = ((temperatura - 273.15) * 9/5) + 32
    print(f"{temperatura}K = {resultado}°F")