# de Speelhaldag

aantalpersonen = 3
prijsticket = 7.45
prijsminuten = 0.370

totaalprijsticket = aantalpersonen * prijsticket
totaalprijsgameseat = aantalpersonen * prijsminuten * 9
totaalprijs = totaalprijsticket + totaalprijsgameseat

print("Dit geweldige dagje-uit met 3 mensen in de Speelhal met 45 minuten VR kost je maar €" + str(totaalprijs))