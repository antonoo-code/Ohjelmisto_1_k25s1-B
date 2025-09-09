"""
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, 
hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. 
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. 
Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. 
(ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)
"""
airports = {}

while True:
    menu = input('Valitse 1: syötä lentoasema, 2: hae lentoasema, 3: lopeta : ')
    if menu == "1":
        port_icaq = input('Syötä lentoaseman ICAQ koodi: ')
        port_name = input('Syötä lentoaseman nimi: ')
        airports[port_icaq] = port_name
    elif menu == "2":
        port_icaq = input('Syötä lentoaseman ICAQ koodi: ')
        if port_icaq in airports:
            print(f'Koodin {port_icaq} lentokenttä on : {airports[port_icaq]}')
        else:
            print('Kenttää ei löydy.')
    elif menu == "3":
        break
    
    
        




