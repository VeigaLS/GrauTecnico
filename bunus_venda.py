nome = input("Nome do vendedor: ")
salario = float(input("Salário: "))
vendas = int(input("Quantidade de Vendas: "))
comissao = 0.15 * salario
print(f"Sua comissão foi de: R$ {comissao:.1f}")
if vendas >= 20:
    print("Parabéns, sua meta foi atingida")