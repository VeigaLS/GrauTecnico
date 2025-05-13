import random
num_sec = random.randint (1,10)
attempts=0
contagem_tentativas=0
num=0
print ("Welcome to game -_Secret Number_-")
print ("Try find the number: ")
while attempts != num_sec:
    num=int(input("Write a number: "))
    contagem_tentativas= contagem_tentativas+1
    if num==num_sec:
        print ("Congratulations!!! You got the secret number right!!!")
        print (f"You needed {contagem_tentativas} tries to get it right")
        break
    elif num < num_sec:
        print ("The secret number is bigger")
    else:
        print ("The secret number is smaller")
        