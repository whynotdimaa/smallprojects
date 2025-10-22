import time
sec = 0
b = 1
while True:
    choice = int(input("Виберіть пункт \n1.Секундомір \n2.Зворотний таймер \n3.exit \n"))
    if choice == 1:
        try:
           while True:
              sec += 1
              time.sleep(1)
              if sec % 60 == 0:
                  print(f"minute {b}")
                  b += 1
                  continue
              print(sec)
        except KeyboardInterrupt:
            print("exit")
    if choice == 2:
        a = int(input("Введіть час відліку: "))
        while a > 0:
            print(a)
            time.sleep(1)
            a -= 1
        print("час вийшов")
    if choice == 3:
        break