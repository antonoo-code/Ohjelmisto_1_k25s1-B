vuosiluku_str = input('Syötä vuosiluku:')
vuosiluku = int(vuosiluku_str)
if vuosiluku % 4 == 0 and vuosiluku % 100 !=0:
    print('Vuosiluku on kaurkausvuosi.1')
elif vuosiluku % 100 == 0 and vuosiluku % 400 == 0 :
    print('Vuosiluku on kaurkausvuosi.')
else:
    print('Vuosiluku ei ole kaurkausvuosi.')