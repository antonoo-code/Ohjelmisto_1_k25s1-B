"""Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
 jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). 
 Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. 
 Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.
"""

seasons = ('talvi' ,'kevät','kesä','syksy')

Month_num = int(input('Syötä kuukauden järjestysnumero (1-12):'))

if Month_num in [12,1,2]:
    print(f'Kuukautesi vuodenaika on : talvi')
elif Month_num in [3,4,5]:
    print(f'Kuukautesi vuodenaika on : kevät')
elif Month_num in  [6,7,8]:
    print(f'Kuukautesi vuodenaika on : kesä')
elif Month_num in [9,10,11]:
    print(f'Kuukautesi vuodenaika on : syksy')

else: 
    print('Kirjoitit virheellisen kuukausi numeron:')


