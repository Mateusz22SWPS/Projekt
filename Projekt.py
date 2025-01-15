from Funkcje import *

koszyk = []
print('Witamy w sklepie Shop top top') 
i = "dalej"
while i == "dalej":
 poddział_dział = main_menu()
 print(poddział_dział)
 if poddział_dział[1] == "dział męski":
  if poddział_dział[0] == "koszulki":
    produkt = product({"czarana koszulka": 50, "niebieska koszulka": 50, "koszulka polo czarna": 70, "koszulka w paski": 55, "bordowa koszulka": 50, "niebieska koszulka polo": 70,  })
    rozmiar = rozmiar()
    print("produkt: ", produkt)
    print("rozmiar: ", rozmiar)
    koszyk = do_koszyka()
i = input("jeśli chcesz kupować dalej wpisz: 'dalej', jeśli nie wpisz cokolwiek")