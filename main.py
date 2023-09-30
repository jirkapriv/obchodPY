rohlikCena = 3
chlebaCena = 20
bagetaMAMAMIA_CENA = 1000
rajceCena = 20
okurkaCena = 20
paprikaCena = 20
pomerancCena = 50
mandarinkaCena = 40
grepfruitCena = 120
cenaCelkemKategorie = 0
celkem = []

shoppingList_pecivo = [["rohlik", 0, rohlikCena], [
    "chleba", 0, chlebaCena], ["bageta", 0, bagetaMAMAMIA_CENA]]
shoppingList_ovoce = [["rajče", 0, rajceCena], [
    "okurka", 0, okurkaCena], ["paprika", 0, paprikaCena]]
shoppingList_zelenina = [["pomeranč", 0, pomerancCena], [
    "mandarinka", 0, mandarinkaCena], ["grepfruit", 0, grepfruitCena]]


def addToList(inp, shoppingList):
    try:
        inp = int(inp)
        print("Zadej počet: ")
        pocet = int(input())
        shoppingList[inp - 1][1] += pocet
    except:
        print("invalid input")

while True:
    print("Vyber kategorii")
    print("1) pečivo ")
    print("2) zelenina ")
    print("3) ovoce ")
    print("4) exit")
    kategorie = input()

    if kategorie == "1":
        while True:
            print("Vyber druh pečiva")
            print("1) rohlík ")
            print("2) chleba ")
            print("3) bageta mamamia")
            print("4) exit")
            inp = input()
            if inp == "1":
                addToList(inp, shoppingList_pecivo)
            if inp == "2":
                addToList(inp, shoppingList_pecivo)
            if inp == "3":
                addToList(inp, shoppingList_pecivo)
            if inp == "4":
                break
    if kategorie == "2":
        while True:
            print("Vyber druh zeleniny")
            print("1) rajče ")
            print("2) okurka ")
            print("3) paprika")
            print("4) exit")
            inp = input()
            if inp == "1":
                addToList(inp, shoppingList_zelenina)
            if inp == "2":
                addToList(inp, shoppingList_zelenina)
            if inp == "3":
                addToList(inp, shoppingList_zelenina)
            if inp == "4":
                break
    if kategorie == "3":
        while True:
            print("Vyber druh ovoce")
            print("1) pomeranč ")
            print("2) mandarinka ")
            print("3) grepfruit")
            print("4) exit")
            inp = input()
            if inp == "1":
                addToList(inp, shoppingList_ovoce)
            if inp == "2":
                addToList(inp, shoppingList_ovoce)
            if inp == "3":
                addToList(inp, shoppingList_ovoce)
            if inp == "4":
                break
    if kategorie == "4":
        break


def inuctenka(listik, cenaCelkemKategorie):
    for x in listik:
        if not x[1] == 0:
            print(f"{x[0]}: {x[1] * x[2]}Kč, počet: {x[1]} ")
            cenaCelkemKategorie += x[1] * x[2]
    celkem.append(cenaCelkemKategorie)


def uctenka(list1, list2, list3, cenaCelkemKategorie):
    inuctenka(list1, cenaCelkemKategorie)
    inuctenka(list2, cenaCelkemKategorie)
    inuctenka(list3, cenaCelkemKategorie)


uctenka(shoppingList_pecivo, shoppingList_ovoce, shoppingList_zelenina, cenaCelkemKategorie)

print(f"Celkem k úhradě: {sum(celkem)}Kč")