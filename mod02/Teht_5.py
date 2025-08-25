Leiviskat_g = float(input('Anna leivisköjen määrä: '))*20 * 32 * 13.3
Naulat_g = float(input('Anna naulojen määrä: '))*32 * 13.3
Luodit_g = float(input('Anna luotejen määrä: '))*13.3
Summa_kg = (Leiviskat_g+Naulat_g+Luodit_g)/1000
kilogrammat = int(Summa_kg)
grammat =(Summa_kg - kilogrammat)*1000
print(f'Massa nykymittojen mukaan: {kilogrammat} kilogrammaa ja {grammat:.2f} grammaa')