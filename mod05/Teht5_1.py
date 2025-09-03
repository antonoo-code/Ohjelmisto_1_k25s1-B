import random



dice_count = int(input('Syötä arpakuutioiden määrä:'))
summa = 0
for noppa_luku in range(dice_count):
    noppa_luku = random.randint(1, 6)
    print(noppa_luku)
    summa += noppa_luku

print(f'yhteenlaskettu summa: {summa}')