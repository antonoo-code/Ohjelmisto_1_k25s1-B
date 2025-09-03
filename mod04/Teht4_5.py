oikea_käyttäjätunnus = 'anton'
oikea_salasana = 'salakala'
yritykset = 0

while yritykset < 5 :
    käyttäjätunnus = input('Syötä käyttäjätunnus:')
    salasana = input('Syötä salasana:')
    while oikea_käyttäjätunnus != käyttäjätunnus or oikea_salasana != salasana :
        yritykset = yritykset + 1
        print('Väärä käyttäjätunnus tai salasana')


    if oikea_käyttäjätunnus == käyttäjätunnus and oikea_salasana == salasana :
        print('Tervetuloa !')
        break






