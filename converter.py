print("Welcome to converter")

while True:
    choice = int(input("Enter your choice: \n1.km to mile/metr \n2.celcium to farengeit \n3.kg to funt/gram \n4.exit \n"))
    if choice == 1:
        choice1 = int(input("Enter your choice: \n1.km to mile \n2.km to metr \n3.metr to km \n4.metr to mile \n5.mile to metr \n6.mile to km \n"))
        if choice1 == 1:
            a = int(input("Введіть число : "))
            mile = a * 0.621371
            print(mile)
        elif choice1 == 2:
            a = int(input("Введіть число : "))
            metr = a * 1000
            print(metr)
        elif choice1 == 3:
            a = int(input("Введіть число : "))
            km = a / 1000
            print(km)
        elif choice1 == 4:
            a = int(input("Введіть число : "))
            mile = a / 1609
            print(mile)
        elif choice1 == 5:
            a = int(input("Введіть число : "))
            metr = a * 1609
            print(metr)
        elif choice1 == 6:
            a = int(input('Введіть число : '))
            km = a / 0.621371
            print(km)
    elif choice == 2:
        choice2 = int(input("Enter your choice: \n1.celcium to farengeit \n2.farengeit to celcium \n"))
        if choice2 == 1:
            a = int(input("Введіть число : "))
            farengeit = (a * 9/5) + 32
            print(farengeit)
        elif choice2 == 2:
            a =int(input("Введіть число : "))
            celcium = (a -32)*5/9
            print(celcium)
    elif choice == 3:
        choice3 = int(input(
            "Enter your choice: \n1.kg to funt \n2.kg to gram \n3.gram to kg \n4.funt to kg \n5.funt to gram \n6.gram to funt \n"))
        if choice3 == 1:
            a = int(input("Введіть число : "))
            funt = a * 2.20462
            print(funt)
        elif choice3 == 2:
            a = int(input("Введіть число : "))
            gram = a * 1000
            print(gram)
        elif choice3 == 3:
            a = int(input("Введіть число : "))
            kg = a / 1000
            print(kg)
        elif choice3 == 4:
            a = int(input("Введіть число : "))
            kg = a / 2.20462
            print(kg)
        elif choice3 == 5:
            a = int(input("Введіть число : "))
            gram = a * 453.592
            print(gram)
        elif choice3 == 6:
            a = int(input('Введіть число : '))
            funt = a / 453.592
            print(funt)
    elif choice == 4:
        break






