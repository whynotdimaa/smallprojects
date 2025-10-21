import json
from pathlib import Path

def loadwords(filepath):
    path = Path(filepath)
    if not path.exists():
        return {}
    with open(filepath, encoding="UTF8-") as f:
        data = json.load(f)
        return data


def savewords(data, filepath):
    path = Path(filepath)
    with open(filepath, "w", encoding="UTF8-", ) as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def addwords(eng, ukr, data):
    data[eng] = ukr
    savewords(data, 'abc.json')
    print(f"Додано : {eng} : {ukr}")


def searchwords(eng, data):
    if eng in data:
        print(f"{eng} : {data[eng]}")
    else:
        print("no one")


def deletewords(eng, data):
    if eng in data:
        del data[eng]
        savewords(data, 'abc.json')
        print("deletesuccess")
    else:
        print("no one")


def showallwords(data):
    for eng, ukr in data.items():
        print(f"{eng} : {ukr}")
data = loadwords('abc.json')
while True:
    print("1. Додати слово")
    print("2. Пошук слова")
    print("3. Видалити слово")
    print("4. Показати всі слова")
    print("5. Вихід")

    choice = int(input())
    if choice == 1:
        a = addwords(input("введіть англ слово : "), input("введіть укр слово : "), data)
    if choice == 2:
        a = searchwords(input("введіть ключ слова(англ)\n"), data)
    if choice == 3:
        a = deletewords(input("введіть ключ слова\n"),data)
    if choice == 4:
        a = showallwords(data)
    if choice == 5:
        exit()



