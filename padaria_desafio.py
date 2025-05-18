import math
frances = integral = doceLiso = doceFarofa = forma = 0
valorFrances = valorIntegral = valorDoceLiso = valorDoceFarofa = valorForma = valortotal = 0.0
def arredondar(valor, casas_decimais):
    return round(valor, casas_decimais)
while True:
    print("______Padaria______")
    print("1 Pão Francês")
    print("2 Pão Integral")
    print("3 Pão Doce Liso")
    print("4 Pão Doce Farofa")
    print("5 Pão de Forma")
    print("6 Fim da compra.")
    print("______________________________")
    opcao = int(input("Escolha sua(s) opção(ões): "))
    if opcao == 1:
        quantidade = int(input("Quantos pães franceses que você quer: "))
        frances += quantidade
        valorFrances += quantidade * 1.04
        valorFrances = arredondar(valorFrances, 2)
    elif opcao == 2:
        quantidade = int(input("Quantos pães integrais que você quer: "))
        integral += quantidade
        valorIntegral += quantidade * 1.04
        valorIntegral = arredondar(valorIntegral, 2)
    elif opcao == 3:
        quantidade = int(input("Quantos pães doces lisos que você quer: "))
        doceLiso += quantidade
        valorDoceLiso += quantidade * 1.08
        valorDoceLiso = arredondar(valorDoceLiso, 2)
    elif opcao == 4:
        quantidade = int(input("Quantos pães farofa que você quer: "))
        doceFarofa += quantidade
        valorDoceFarofa += quantidade * 1.11
        valorDoceFarofa = arredondar(valorDoceFarofa, 2)
    elif opcao == 5:
        quantidade = int(input("Quantos pães de forma que você quer: "))
        forma += quantidade
        valorForma += quantidade * 0.95
        valorForma = arredondar(valorForma, 2)
    elif opcao == 6:
        valortotal = valorFrances + valorIntegral + valorDoceLiso + valorDoceFarofa + valorForma
        valortotal = arredondar(valortotal, 2)
        break
    else:
        print("Opção inválida. Tente outra vez")
print("Resumo:")
if frances > 0:
    print(f"Pão Francês - Quantidade: {frances} | Valor: R$ {valorFrances:.2f}")
if integral > 0:
    print(f"Pão Integral - Quantidade: {integral} | Valor: R$ {valorIntegral:.2f}")
if doceLiso > 0:
    print(f"Pão Doce Liso - Quantidade: {doceLiso} | Valor: R$ {valorDoceLiso:.2f}")
if doceFarofa > 0:
    print(f"Pão Doce Farofa - Quantidade: {doceFarofa} | Valor: R$ {valorDoceFarofa:.2f}")
if forma > 0:
    print(f"Pão de Forma - Quantidade: {forma} | Valor: R$ {valorForma:.2f}")
print(f"Valor da compra: R$ {valortotal:.2f}")