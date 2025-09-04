"""
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
 kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
"""
import math

def calc_unitprice(diameter_m, price_e):
    return price_e / (math.pi*(diameter_m/2)**2)


pizza1_dia = float(input('Syötä ensimmäisen pizzan halkaisija metreinä: '))
pizza1_price = float(input('Syötä ensimmäisen pizzan hinta euroina: '))
pizza2_dia = float(input('Syötä toisen pizzan halkaisija metreinä: '))
pizza2_price = float(input('Syötä toisen pizzan hinta euroina: '))

pizza1_unitprice = calc_unitprice(pizza1_dia, pizza1_price)
pizza2_unitprice = calc_unitprice(pizza2_dia, pizza2_price)
if pizza1_unitprice > pizza2_unitprice:
    print('Pitsa 2 on wörtimpi!!!')
elif pizza2_unitprice == pizza1_unitprice:
    print('The pizzaz are yhtä wörtit!!')
else:
    print('Pitsa 1 on wörtimpi!!!')


    


    
