notaP= float(input("Digite sua nota da prova: "))
notaT = float (input("Digite sua nota do trabalho: "))
media= (notaP+notaT)/2
print (f"Sua nota é: {media}")
if media<7:
    print ("Reprovado!")
else:
    print("Aprovado!!!")