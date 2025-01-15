from Funkcje import *

koszyk = []
print('Witamy w sklepie Shop top top') 
i = "dalej"
koszyk = []
while i == "dalej":
 poddział_dział = main_menu()
 if poddział_dział[1] == "dział męski":
  if poddział_dział[0] == "koszulki":
    produkt = product({"czarana koszulka": 50, "niebieska koszulka": 50, "koszulka polo czarna": 70, "koszulka w paski": 55, "bordowa koszulka": 50, "niebieska koszulka polo": 70, "zielona koszulka polo":70, "czaran koszula":90, "biała koszula":90})
    print(produkt)
    rozmiar = size()
    print(f"produkt: {produkt[0]} - ", produkt[1])
    print("rozmiar: ", rozmiar)
    produkt.append(rozmiar)
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "spodnie":
    produkt = product({"jeansy czarne":70, "jeansy czarne z przetarciami":80, "jeansy granatowe":70, "jeansy granatowe z przetarciami":80, "jeansy białe":70, "jeansy białe z przetarciami":80, "jeansy jasne niebieskie":70, "jeansy jasne niebieskie z przetarciami": 80})
    print(produkt)
    rozmiar = size()
    print(f"produkt: {produkt[0]} - ", produkt[1])
    produkt.append(rozmiar)
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "bluzy":
    produkt = product({"bluza czarna z kapturem":100, "bluza biała z kapturem":100, "bluza niebieska z kapturem":100, "bluza czerwona z kapturem":100, "bluza czarna":90, "bluza biała":90, "bluza niebieska":90, "bluza czerwona": 90})
    produkt = product({"czarne spodnie Sport":60,\
      "szare spodnie Sport":60"bordowe spodnie Sport":60,\
      "niebieskie spodnie Sport":60,"czarne spodnie Classic":70,\
      "szare spodnie Classic":70, "bordowe spodnie Classic":70,\
      "białe spodnie Classic":80})
    print(produkt)
    rozmiar = size()
    print(f"produkt: {produkt[0]} - ", produkt[1])
    print("rozmiar: ", rozmiar)
    produkt.append(rozmiar)
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "kurtki":
    produkt = product({"kurtka zimowa czarna":120, "kurtka zimowa biła":120, "kurtka jesienna czarna":100, "kurtka jesienna biała":100, "płaszcz brązowy":120, "płaszcz czarny":120, "płaszcz zimowy czarny":140, "płaszcz zimowy brązowy":140})
    print(produkt)
    rozmiar = size()
    print(f"produkt: {produkt[0]} - ", produkt[1])
    produkt.append(rozmiar)
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "akcesoria":
    produkt = product({"skarpety 3-pak":50, "bokserki 3-pak":50, "pasek czarny":60, "pasek brązowy":60, "perfumy":80, "naszyjnik z krzyżem":30, "sygnety 3-pak": 50})
    print(produkt)
    print(f"produkt: {produkt[0]} - ", produkt[1])
    koszyk.append(do_koszyka(produkt))
 elif poddział_dział[1] == "dział dziecięcy":
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
  elif poddział_dział[0] == "kurtki":
    produkt = product({"zimowa": 88, "letnia": 130, "czarna letnia": 67, "jesienna": 66, "jesienno-zimowa": 67, "gruba zimowa": 40, "na narty": 20})
    print(produkt)
    rozmiar = size()
    print(f"produkt: {produkt[0]} -", produkt[1])
    print("rozmiar: ", rozmiar)
    produkt.append(rozmiar)
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "akcesoria":
    produkt = product({"bielizna": 88, "skarpety": 130, "spinki": 67, "naszyjniki": 66, "gumki": 67, "zegarki": 40, "perfumy": 20, "paski": 10})
    print(produkt)
    print(f"produkt: {produkt[0]} -", produkt[1])
    koszyk.append(do_koszyka(produkt))
 elif poddział_dział[1] == "dział zwierzęcy":
  if poddział_dział[0] == "pies":
    produkt = product ({"karma morka 1kg": 30, "karma sucha 1kg": 30, "przysmaki": 10, "obroża dla dużego psa": 15, "obroża dla małego psa": 10, "kurta zimowa dla dużego psa": 40, "kurta dla małego psa": 35, "gryzak w kształcie kości": 20, "smycz": 10 })
    print(f"produkt: {produkt[0]} - ", produkt[1])
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "kot":
    produkt = product ({"karma mokra 1kg": 30, "karma sucha 1kg":30, "przysmaki": 10, "drapak": 40, "żwirek 2kg": 25, "kuweta": 45, "wędka": 15, "legowisko": 50 })  
    print(f"produkt: {produkt[0]} - ", produkt[1])
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "ptaki": 
    produkt = product ({"karma 100 sztuk/90g": 30, "karma 50sztul/90g": 20, "klatka małą": 20, "klatka duża": 35, "wiszący most": 8, "zabawka do dzubania": 10 })
    print(f"produkt: {produkt[0]} - ", produkt[1])
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "ryby":
    produkt = product ({"pokarm w płatkach 250ml": 15, "pokarm w płatach 500ml": 20, "akwarium małe": 50, "akwrium duże": 70, "filtr": 100 })  
    print(f"produkt: {produkt[0]} -" , produkt[1])
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "gryzonie":
    produkt = product ({"płatki grochu 250g": 15, "płatki grochu 500ml": 25, "klatka mała": 35, "klatka duża": 50, "bela siana 250g": 20, "bela siana 500g": 30, "domek z siana": 25, "tunel z siana": 15, "koło do biegania": 20}) 
    print(f"produkt: {produkt[0]} - ", produkt[1]) 
    koszyk.append(do_koszyka(produkt)) 
 elif poddział_dział[1] == "dział kobiecy":
  if poddział_dział[0] == "bluzy":
    produkt = product({"biała bluza":70, "białą bluza z zamkiem":90,\
     "czarna bluza":70, "czarna bluza z zamkiem":90, "niebieska bluza":70,\
     "niebieska bluza z zamkiem":90, "bordowa bluza":80,\
     "bordowa bluza z zamkiem":100})
    print(produkt)
    rozmiar = size()
    print(f"produkt: {produkt[0]} - ", produkt[1])
    print("rozmiar: ", rozmiar)
    produkt.append(rozmiar)
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "spodnie":
    produkt = product({"czarne spodnie Sport":60,\
      "szare spodnie Sport":60"bordowe spodnie Sport":60,\
      "niebieskie spodnie Sport":60,"czarne spodnie Classic":70,\
      "szare spodnie Classic":70, "bordowe spodnie Classic":70,\
      "białe spodnie Classic":80})
    print(produkt)
    rozmiar = size()
    print(f"produkt: {produkt[0]} - ", produkt[1])
    print("rozmiar: ", rozmiar)
    produkt.append(rozmiar)
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "kurtki":
    produkt == product({"biała kurtka Short":220, \
      "czarna kurtka Short":220, "bordo kurtka Short":220, \
      "biała kurtka Long":290, "czarna kurtka Long":290,\
      "bordo kurtka Long":290, "szara kurtka Medium":250})
    print(produkt)
    rozmiar = size()
    print(f"produkt: {produkt[0]} - ", produkt[1])
    print("rozmiar: ", rozmiar)
    produkt.append(rozmiar)
    koszyk.append(do_koszyka(produkt))
  elif  poddział_dział[0] == "koszulki":
   produkt == product({"czarna koszulka Sport":150,\
     "niebieska koszulka Sport":150, "biała koszulka Sport":150, \
     "bordowa koszulka Sport":150,"czarna koszulka Classic":190,\
     "niebieska koszulka Classic":190, "bordowa koszulka Classic":190, \
     "biała koszulka Classic":180}) 
   print(produkt)
   rozmiar = size()
   print(f"produkt: {produkt[0]} - ", produkt[1])
   print("rozmiar: ", rozmiar)
   produkt.append(rozmiar)
   koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "akcesoria":
   produkt == product({"czarne rękawiczki Skóra naturalna":250,\
     "czarne rękawiczki Skóra ekologiczna":190, "kosmetyczka S Light":30,\
     "kosmetyczka M Light":40, "kosmetyczka L Light":60,\
     "kosmetyczka S Dark":30,"kosmetyczka M Dark":40, \
     "kosmetyczka L Dark":60, "czarny szalik Jedwab":300, \
     "biały szalik Jedwab":300,"perłowy naszyjnik":400, "naszyjnik Wianek Koniczyny":350, "wisiorek Kropla":350}) 
   print(produkt)
   print(f"produkt: {produkt[0]} - ", produkt[1])
   koszyk.append(do_koszyka(produkt))

 i = input("jeśli chcesz kupować dalej wpisz: 'dalej', jeśli chcesz przejść do koszyka wpisz 'koszyk': ")

koszyk = [x for x in koszyk if x is not None]
print("------------")
print(koszyk)
print("------------")
czy_się_zgadza = input("czy wszystko sie zgadza w koszyku, wpisz 'tak' lub 'nie': ")
zgadza = "tak"
while zgadza == "tak":
 if czy_się_zgadza == "nie":
  for i in range(len(koszyk)):
    print(f"{i}. {koszyk[i]}")
  który = input("który produkt się nie zgadza: ")
  del koszyk[int(który) - 1]
 else:
  break
 zgadza = input("czy już wszystko się zgadza ('tak','nie'): ")
suma = 0
for i in range(len(koszyk)):
   suma = suma + koszyk[i][1]
print("------------")
print(f"do zapłaty: {suma}")
  
list = ["karta płatnicza", "PayPal", "Blik", "Bitcoin"]
płatność = input("jaki chcesz rodzaj płatności:")
print('')
for i in range(len(list)):
  print(f"{i + 1}. {list[i]}")
print('')

dostawy = ["kurier", "paczkomat", "poczta", "odbiór osobisty"]
dostawa = input("jaki chcesz rodzaj dostawy: ")
print('')
for i in range(len(dostawy)):
  print(f"{i + 1}. {dostawy[i]}")
print('')
print(f"rodzaj dostawy: {dostawy[int(dostawa) - 1]}")

print("-----------")
Imie = input("podaj imie: ")
Nazwisko = input("podaj nazwisko: ")
Nr_telefonu = input("podaj nr telefonu: ")
Ulica = input("podaj ulicę: ")
Nr_domu = input("podaj nr domu: ")
Miasto = input("podaj miasto zamieszkania: ")
Kod_pocztowy = input("podaj kod pocztowy: ")
Nr_mieszkania = input("podaj nr mieszkania: ")
print("-------------")
print('')
print("Podsumowanie zamówienia:")
print(f"koszyk: {koszyk}" + "\n" + f"do zapłaty: {suma}zł" + \
      "\n" + f"metoda płatności: {list[int(płatność) - 1]}" + "\n" + f"rodzaj dostawy: {dostawy[int(dostawa) - 1]}" + \
      "\n" + "dane do wysyłki: " + "\n" + f"Imie: {Imie}" + "\n" + f"Nazwisko: {Nazwisko}" +\
      "\n" + f"numer telefonu: {Nr_telefonu}" + "\n" + f"Ulica: {Ulica}" + '\n' + f"Numer domu: {Nr_domu}" +\
      "\n" + f"numer mieszkania: {Nr_mieszkania}"+ "\n" + f"Miasto: {Miasto}" + "\n" + f"Kod pocztowy: {Kod_pocztowy}")