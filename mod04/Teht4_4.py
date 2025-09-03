#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
#Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
#Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
#Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
import random
#kysy N arvo käyttäjältä
oikea = random.randint(1,10)

arvattu = int(input('Arvaa kokonaisluku:'))
while oikea != arvattu :
    if oikea < arvattu :
        print('Liian suuri arvaus.')
        arvattu =int(input('Arvaa uudestaan:'))
    elif oikea > arvattu :
        print('Liian pieni arvaus.')
        arvattu = int(input('Arvaa uudestaan:'))

    if oikea == arvattu :
        print('Oikein arvattu!')
