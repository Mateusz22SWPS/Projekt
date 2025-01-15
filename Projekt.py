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
    print("rozmiar: ", rozmiar)
    produkt.append(rozmiar)
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "bluzy":
    produkt = product({"bluza czarna z kapturem":100, "bluza biała z kapturem":100, "bluza niebieska z kapturem":100, "bluza czerwona z kapturem":100, "bluza czarna":90, "bluza biała":90, "bluza niebieska":90, "bluza czerwona": 90})
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
    print("rozmiar: ", rozmiar)
    produkt.append(rozmiar)
    koszyk.append(do_koszyka(produkt))
  elif poddział_dział[0] == "akcesoria":
    produkt = product({"skarpety 3-pak":50, "bokserki 3-pak":50, "pasek czarny":60, "pasek brązowy":60, "perfumy":80, "naszyjnik z krzyżem":30, "sygnety 3-pak": 50})
    print(produkt)
    print(f"produkt: {produkt[0]} - ", produkt[1])
    koszyk.append(do_koszyka(produkt))
 i = input("jeśli chcesz kupować dalej wpisz: 'dalej', jeśli chcesz przejść do koszyka wpisz 'koszyk': ")

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