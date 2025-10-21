print("welcome to calculator ")
menu = {1 : "Вираз", 2 : "Калькулятор", 3: "Вихід"}


while True:
    print(menu)
    choice = int(input("enter your choice : "))
    if choice == 1:
        expression = input("enter your expression : ")
        result = eval(expression)
        print(result)
    elif choice == 2:
        try:
            o = input("Enter a operator: ")
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if o == "+":
                print(a + b)
            if o == "-":
               print(a - b)
            if o == "*":
               print(a * b)
            if o == "/":
                try:
                   print(a / b)
                except ZeroDivisionError:
                    print("division by zero")
            if o == "//":
               print(a // b)
            if o == "**":
               print(a ** b)
        except ValueError:
               print("Invalid input")
    elif choice == 3:
        break
    else:
        print("invalid input")
