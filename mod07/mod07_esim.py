"""
Monikko, eli (tuple) on , kuin lista jota ei voida muokata.
"""

list = [1,2,3,4,5,6]
print(list)

"""
monikon voi luoda ilman sulkeita.
Monikko voi sisältää erilaista tietoa.
"""


monikko = (1,2,3,4,5,6)
print(monikko)
monikko2 = 1,2,'Anton',(3,4),88
print(monikko2)

"""
Luetaan listan ensimmäinen alkio
"""
print(list[0])
print(monikko[0])


"""
Toisinkun lista monikkoa ei voi lisätä tai poistaa alkioita luonnin jälkeen. Monikosta voi hakea indeksin 
avulla alkion arvo
"""

list[0] = 0
list.append(7)
print('Muokattu lista', list)


viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")


sanat = ('eka','toka','kolmas','neljäs')
for sana in sanat:
    if sana == 'kolmas':
        print(sana) 


"""
Monikon arvo purku muuttujiin
"""
hedelmät = ("Appelsiini", "Banaani", "Omena")
(eka, toka, kolmas) = hedelmät
print (f"Hedelmiä ovat {eka}, {toka} ja {kolmas}.")

#monikon voi antaa funktiolle parametriksi


def tulosta_monikko(h):
    for h in hedelmät:
        print(h)


tulosta_monikko(hedelmät)

#Monikko funktion paluuarvona.

import random


def heitä():
    eka =  print(random.randint)
    toka = print(random.randint(1,6))
    print(eka, toka)

#yksinkertaistetaan random

import random

def heitä():
    eka, toka = random.randint(1,6), random.randint(1,6)
    return eka, toka

noppa1, noppa2 = heitä()
print(f"Nopista tuli {noppa1} ja {noppa2}.")

#joukko eli set {}
#alkioihin ei voi viitata indeksillä.
#alkio vain kertaalleen
#joukko merkataan aaltosulkeilla

joukko = {1,2,3,4,5,6}
print('summa', sum(joukko))

#voiko joukkoa käyttää laskemiseen esim jos kysytään 50  ihmiseltä iät jos on samat ei tallenna 
#halutaan tietää kuinka monta eri ikäistä ihmistä on 50 ihmisessä.
#lopuks listaa eri iät ja niiden summat.

#autolista 

autolista = []
autolista.append ('Audi')
print(autolista)
print(type(autolista))

autojoukko = set()
autojoukko.add('Mersu')
print(type(autojoukko))

#jos yrität luoda tyjää joukkoa {} sulkeilla tästä tulee sanakirja

autosanakirja = {}
print(type(autosanakirja))

#kun sanakirja alustetaan anntetaan avain-arvopari
#seuraavasti: AVAIN : arvo
#peräkkäiset avainarvoparit erotellaan pilkulla.

oppilaat = {'Eero': 21, 'Nicke' : 27, 'Anton': 23}
print(oppilaat)

#mitä ovat tietueet / items
print(oppilaat.items())

##mitä ovat avaimet

print(oppilaat.keys())

print(oppilaat.values())


#kierrosmuuttuja eli tässätapauksessa o saa arvokseen kunkin sanakirjassa esiintyvän avaimen ei koko paria.
for o in oppilaat:
    print(o)

oppilaat['Anton']
print('etsitään avaimella Antonin ikä:', oppilaat['Anton'])    