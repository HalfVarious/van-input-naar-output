print("=======================================================================================")
print("                Welkom bij pizzaria Salami! Plaats hier uw bestelling.")
print("=======================================================================================")




prijssmall = 4.50
prijsmedium = 6.00
prijslarge = 7.50

aantalsmall = int(input(f"Hoeveel small pizza's wilt u? (€{prijssmall}) : "))
aantalmedium = int(input(f"Hoeveel medium pizza's wilt u?(€{prijsmedium}) : "))
aantallarge = int(input(f"Hoeveel large pizza's wilt u?(€{prijslarge}) : "))

totaalprijs = prijssmall * aantalsmall + prijsmedium * aantalmedium + prijslarge * aantallarge

print(f"{aantalsmall} Small: € {prijssmall*aantalsmall} ")
print(f"{aantalmedium} Medium: € {prijsmedium*aantalmedium}")
print(f"{aantallarge} Large: € {prijslarge*aantallarge}")
print("=======================================================================================")
print(f"          Je bestelling is in totaal : €{totaalprijs} , U kunt contant en met PIN betalen!")
print("=======================================================================================")