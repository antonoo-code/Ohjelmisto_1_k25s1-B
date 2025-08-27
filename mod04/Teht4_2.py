#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
#Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm break loopista ulos
tuuma = float(input('Syötä tuumien lukumäärä:'))
while tuuma > 0 :
    print(f"Syöttämäsi tuuma määrä on {tuuma * 2.54 } senttimetriä")
    tuuma = float(input('Syötä tuumien lukumäärä:'))
    
