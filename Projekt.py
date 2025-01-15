from Funkcje import *

print('Witamy w sklepie Shop top top') 
poddział_dział = main_menu()
print(poddział_dział)
if poddział_dział[1] == "dział męski":
  if poddział_dział[0] == "koszulki"
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