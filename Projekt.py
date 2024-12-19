def product(produkt):
    print("poddziały: \n" + "\n".join(produkt))
    wybór_produktu = input("wybierz produkt: ")
    produkt = produkt[int(wybór_produktu) - 1]
    return produkt

def size():
    rozmiar = ["S", "M", "L", "XL"]
    print("poddziały: \n" + "\n".join(rozmiar))
    wybór_rozmiaru = input("wybierz poddział: ")
    rozmiar = rozmiar[int(wybór_rozmiaru) - 1]
    return rozmiar

def sub_section(poddział):
    print("poddziały: \n" + "\n".join(poddział))
    wybór_poddziału = input("wybierz poddział: ")
    poddział = poddział[int(wybór_poddziału) - 1]
    return poddział

def main_menu():
    dział = ["dział męski", "dział kobiecy", "dział dziecięcy", "dział zwierzęcy"]
    print("działy: \n" + "\n".join(dział))
    wybór_działu = input("wybierz dział: ")
    dział = dział[int(wybór_działu) - 1]
    if dział == "dział męski" or dział == "dział kobiecy" or dział == "dział dziecięcy":
       poddział = sub_section(["koszulki", "spodnie", "bluzy", "kurtki", "akcesoria"])
    else :
       poddział = sub_section(["obroże", "karma", "zabawki", "ubrania"])
    return poddział, dział

print('Witamy w sklepie Shop top top') 
poddział_dział = main_menu()
print(poddział_dział)
#if poddział_dział[1] == "dział męski":
 #  if poddział_dział[0] == "koszulki"
