def product(produkt):
    lista_kluczy = list(produkt.keys())
    print("produkty: \n")
    for i in range(len(lista_kluczy)):
     print(f"{i + 1}. {lista_kluczy[i]} - {produkt[lista_kluczy[i]]}")
    print(" ")
    wybór_produktu = input("wybierz produkt: ")
    print("------------")
    produkt = [lista_kluczy[int(wybór_produktu) - 1], produkt[lista_kluczy[int(wybór_produktu) - 1]]]
    return produkt

def size():
    rozmiar = ["S", "M", "L", "XL"]
    print("------------")
    print("rozmiary: \n")
    for i in range(len(rozmiar)):
     print(f"{i + 1}. {rozmiar[i]}")
    print(" ")
    wybór_rozmiaru = input("wybierz rozmiar: ")
    print("------------")
    rozmiar = rozmiar[int(wybór_rozmiaru) - 1]
    return rozmiar

def sub_section(poddział):
    print("------------")
    print("poddziały: ")
    print("\n")
    for i in range(len(poddział)):
     print(f"{i + 1}. {poddział[i]}")
    print(" ")
    wybór_poddziału = input("wybierz poddział: ")
    print("------------")
    poddział = poddział[int(wybór_poddziału) - 1]
    return poddział

def main_menu():
    dział = ["dział męski", "dział kobiecy", "dział dziecięcy", "dział zwierzęcy"]
    print("------------")
    print("działy: \n")
    for i in range(len(dział)):
     print(f"{i + 1}. {dział[i]}")
    print(" ")
    wybór_działu = input("wybierz dział: ")
    print("------------")
    dział = dział[int(wybór_działu) - 1]
    if dział == "dział męski" or dział == "dział kobiecy" or dział == "dział dziecięcy":
       poddział = sub_section(["koszulki", "spodnie", "bluzy", "kurtki", "akcesoria"])
    else :
       poddział = sub_section(["pies", "kot", "ptaki", "ryby", "gryzonie"])
    return poddział, dział

def do_koszyka(produkt):
    print("------------")
    x = input("czy chcesz dodać to do koszyka, wpisz 'tak' lub 'nie': ")
    print(" ")
    if x == "tak":
       return produkt
    else:
       pass


