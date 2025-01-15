from Funkcje import *

print('Witamy w sklepie Shop top top') 
poddział_dział = main_menu()
print(poddział_dział)
if poddział_dział[1] == "dział męski":
  if poddział_dział[0] == "koszulki":
elif poddział_dział[1] == "dział dzieciecy":
  if poddział_dział[0] == "spodnie":
    produkt = product({"jeansy czarne": 50, "jeansy czerwone":70, "jeansy żółte": 30, "czerwone dresy": 40, "szare dresy": 80, "niebieskie dresy": 44, "jeansy": 68, "rurki": 50, "bojówki": 33, "fioletowe dresy": 78})
    print(produkt)
    rozmiar = size()
    print(f"produkt: {produkt[0]} -", produkt[1])
    print("rozmiar: ", rozmiar)
    produkt.append(rozmiar)
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "bluzy":
    produkt = product({"żółta sportowa": 20, "biało-szara z kapturem": 68, "czarno-żółta bez kapturu": 46, " pomarańczowa bluza kangur": 100, " fioletowa na codzień": 120, "kolorowa rozpinana": 78, "ciemno szara przez głowę": 89, "czarna z kapturem": 60, "zielona rozpinana": 99, "ciemno szara na codzień": 88, "biało-czerwona sportowa": 54})
    print(produkt)
    rozmiar = size()
    print(f"produkt: {produkt[0]} -", produkt[1])
    print("rozmiar: ", rozmiar)
    produkt.append(rozmiar)
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "koszulki":
    produkt = product({"z krótkim rękawem": 88, "z długim rękawem": 130, "oversize": 67, "z dekoltem": 66, "czarna oversize": 67, "biała maxi": 40, "zielona longsleeve": 20, "fioletowa klasyczna": 10, "niebieska elegancka": 30, "klasyczna ze wsorem": 33})
    print(produkt)
    rozmiar = size()
    print(f"produkt: {produkt[0]} -", produkt[1])
    print("rozmiar: ", rozmiar)
    produkt.append(rozmiar)
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "akcesoria":
    produkt = product({"bielizna": 88, "skarpety": 130, "spinki": 67, "naszyjniki": 66, "gumki": 67, "zegarki": 40, "perfumy": 20, "paski": 10})
    print(produkt)
    rozmiar = size()
    print(f"produkt: {produkt[0]} -", produkt[1])
    print("rozmiar: ", rozmiar)
    produkt.append(rozmiar)
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "kurtki":
    produkt = product({"zimowa": 88, "letnia": 130, "czarna letnia": 67, "jesienna": 66, "jesienno-zimowa": 67, "gruba zimowa": 40, "na narty": 20})
    print(produkt)
    rozmiar = size()
    print(f"produkt: {produkt[0]} -", produkt[1])
    print("rozmiar: ", rozmiar)
    produkt.append(rozmiar)
    koszyk.append(do_koszyka(produkt))