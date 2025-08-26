#valintarakenne-esimerkkejä (mod3)
#aina kun on yhtäsuurinkuin vertailu kaksi ==
#onko_totta = False
import random



satunnaisluku = random.randint(0,100)

if satunnaisluku > 50:
    print('Kruuna!')
elif satunnaisluku <= 50:
    print('Klaava!')
else:
    print('kolikko jäi pystyyn.')

oikea_salasana = 'salakala'
tunnus = 'Anton'
input_tunnus = input('Anna tunnus: ')
input_salasana = input('Anna salasana: ')

if input_tunnus == tunnus and input_salasana == input_salasana:
    print('Tervetuloa!')
    kehote = input('Mitäs haluat tehdä?')
    if kehote == "Ruveta uhkapelaamaan":
        print('Tässä osoite : Veikkaus.fi')
    else:
        print('en ymmärtänyt kehotetta')
else:
    print('Väärä salasana')

print('ohjelma suljettu. Heippa!')




