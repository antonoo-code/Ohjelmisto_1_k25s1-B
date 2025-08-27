loppu = 1000
laskuri = 0
kolmella_jaolliset = laskuri % 3 == 0

while laskuri < loppu:
    laskuri = laskuri + 1
    if laskuri % 3 == 0:
        print(f'Luku {laskuri} on kolmella jaollinen ')
