# Feestlunch

AantalCroissantjes = 17
AantalStokbroden = 2 
AantalKorting = 3

PrijsCroissantjes = 0.39
PrijsStokbroden = 2.78
PrijsKorting = -0.50

TotaalprijsCroissantjes = AantalCroissantjes * PrijsCroissantjes
TotaalprijsStokbroden = AantalStokbroden * PrijsStokbroden
Korting = AantalKorting * PrijsKorting

totaalprijs = TotaalprijsCroissantjes + TotaalprijsStokbroden + Korting

print("De feestlucnh kost je bij de bakker €" + str(totaalprijs) + " voor de 17 croissantjes en de 2 stokboden als de 3 kortingsbonnen nog geldig zijn")