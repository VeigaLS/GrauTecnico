sum=0
number=1
while number !=0:
    number=int(input("Enter a number (0 for Exit): "))
    sum= sum+number
    if number !=0:
        print(f"The sum so far: {sum}")
print(f"The total of sum is: {sum}")       