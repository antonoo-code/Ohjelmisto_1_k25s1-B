""" 
Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon. 
Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa. 
Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.
 """

names = set()


input_name = input('Syötä nimi: ')
while input_name != "" :
    if input_name not in names:
        print('uusi nimi')
        names.add(input_name)
    else:
        print('Aiemmin syötetty nimi')
    input_name = input('Syötä nimi: ')
