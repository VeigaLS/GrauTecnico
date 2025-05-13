option = 0
while option !=5:
    print ("__Menu__")
    print ("1 - Hamburguer")
    print ("2 - Pizza")
    print ("3 - Salad")
    print ("4 - Soda")
    print ("5 - Sair")
    print ("Enter a key 1-4 press 5 to exit")
    option = int(input("Choice an option: "))
    if option ==1:
        print ("You choose hamburguer")
    elif option ==2:
        print ("You choose pizza")
    elif option ==3:
        print ("You choose salad")
    elif option ==4:
        print ("You choose soda")
    elif option ==5:
        print ("Exiting for menu...")
        break
    else:
        print ("Invalid option. Try again")