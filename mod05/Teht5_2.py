

luku = []

for i in range(100000):
    luku_s = input('Syötä luku:')
    if luku_s == '':
        break
    luku.append(int(luku_s))
luku.sort(reverse=True)
for i in range (0,5):
    print(f'Viisi suurinta lukua: {luku[i]} ')

