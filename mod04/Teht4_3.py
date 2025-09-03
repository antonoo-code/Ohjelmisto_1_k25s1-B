#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
totuus = True
tyhja_merkkijono = ''
luku = []
while totuus :
    syöte =input('Syötä luku:')

    if syöte != tyhja_merkkijono :
        luku.append(float(syöte))

    else:
        print(f'Isoin syötetty luku: {min(luku)}')
        print(f'Pienin syötetty luku: {max(luku)}')
        totuus = False

