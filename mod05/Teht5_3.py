#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

luku = int(input('Syötä luku:'))
alkuluku = True

for i in range(2,luku):
    if luku % i == 0:
        alkuluku = False

if alkuluku:
    print('alkuluku')

else:
    print('ei alkuluku')
