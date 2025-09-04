#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
#Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, 
#kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.

def galloncalc (g):
    liters = g * 3.785
    return liters

    
    

while True:
    gasoline_g = float(input('Syötä bensan määrä galloneina:'))
    calc = galloncalc(gasoline_g)
    if calc < 0:
        break
    else:
        print(f'Syötetyt gallonit litroina: {calc}')




    
