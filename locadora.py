custodia = 90.0
custokm = 0.20
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("              Preços")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print(f"Custo por dia: R$ {custodia}")
print(f"Custo por km rodado: R$ {custokm}")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
kmper = float(input("Km's percorridos: "))
diasalug = int(input("Quantidade de dias alugados: "))
precodias = diasalug * custodia
precokm = kmper * custokm
precototal = precodias + precokm
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("RECIBO DE ALUGUEL")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print(f"Dias alugados: {diasalug} dias")
print(f"Custo dos dias: R$ {precodias}")
print(f"Quilômetros percorridos: {kmper} km")
print(f"Custo dos Quilômetros: R$ {precokm:.1f}")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print(f"Preço total a pagar: R$ {precototal}")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")