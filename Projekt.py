from Funkcje import *

print('Witamy w sklepie Shop top top') 
poddział_dział = main_menu()
print(poddział_dział)
if poddział_dział[1] == "dział męski":
  if poddział_dział[0] == "koszulki":
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